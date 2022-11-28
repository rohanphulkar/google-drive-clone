from django.shortcuts import render,HttpResponse,redirect
from pathlib import Path
from .models import Folder,File
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(user=request.user,parent=None)
        files = File.objects.filter(folder=None,user=request.user)
        return render(request, 'drive/home.html',{"folders": folders, "files": files})
    else:
        return redirect('login')

def file_upload_home(request):
    if request.method=="POST":
        if request.FILES:
            file = request.FILES['file-input']
            file_name = str(request.FILES['file-input'])
            file = File.objects.create(file=file,name=file_name,user=request.user)
    return redirect('home')
def file_upload(request,id):
    if request.method=="POST":
        if request.FILES:
            file = request.FILES['file-input']
            file_name = str(request.FILES['file-input'])
            folder = Folder.objects.get(uuid=id)
            file = File.objects.create(file=file,name=file_name,folder=folder,user=request.user)
    return redirect('folder',id=id)

def create_folder_home(request,id=None):
    if request.user.is_authenticated:
        if request.method=="POST":
            name = request.POST.get('folder_name_home')
            folder = Folder.objects.create(user=request.user,parent=None,name=name)
            return redirect('home')
    else:
        return redirect('login')

def folder(request,id=None):
    if request.user.is_authenticated:
        folder = Folder.objects.filter(uuid=id)
        if folder:
            folders = Folder.objects.filter(user=request.user,parent=id)
            files = File.objects.filter(folder=id,user=request.user)
            return render(request, 'drive/folder.html',{"folders": folders,"files":files,"id":id,"folder_name":folder.first().name})
        else:
            return redirect('home')

    else:
        return redirect('login')

def create_folder(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            name = request.POST.get('folder_name')
            folder = Folder.objects.get(uuid=id)
            new_folder = Folder.objects.create(user=request.user,parent=folder,name=name)
            return redirect('folder',id=id)
    else:
        return redirect('login')