from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
import uuid
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if " " in full_name:
                first_name = full_name.split(' ')[0]
                last_name = full_name.split(' ')[1]
            else:
                first_name = full_name
                last_name = ""
            check_user = User.objects.filter(email=email)
            if check_user:
                return redirect('login')
            user = User.objects.create(first_name=first_name,last_name=last_name,email=email)
            uid = uuid.uuid4().hex
            token = str(uid)
            user.set_password(password)
            user.verification_token = token
            user.save()
            send_mail(
                'R-cloud Email Verification',
                f"click on this link to verify your account http://localhost:8000/accounts/verified/{str(user.uuid)}/{token}/",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return redirect('verification_sent')
            

        return render(request, 'accounts/register.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(
                username=email,
                password=password,
            )
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        return render(request, 'accounts/login.html')

@login_required(login_url='/login/')
def logoutPage(request):
    logout(request)
    return redirect('home')
    

def verification_sent(request):
    return render(request, 'accounts/verification_sent.html')

def verified(request,uid,token):
    user = User.objects.get(uuid=uid)
    if user.verification_token == token:
        user.is_verified = True
        user.save()
        return render(request,'accounts/verified.html')
    else:
        return redirect('register')