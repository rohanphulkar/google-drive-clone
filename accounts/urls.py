from django.urls import path
from .views import register,loginPage,logoutPage,verification_sent,verified
urlpatterns = [
    path("register/",register,name="register"),
    path("login/",loginPage,name="login"),
    path("logout/",logoutPage,name="logout"),
    path("verification_sent",verification_sent,name="verification_sent"),
    path("verified/<str:uid>/<str:token>/",verified,name="verified"),

]
