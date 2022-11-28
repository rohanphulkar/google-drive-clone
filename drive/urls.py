from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path("file_upload_home/",views.file_upload_home,name="file_upload_home"),
    path("file_upload/<str:id>/",views.file_upload,name="file_upload"),
    path("folder/<str:id>/",views.folder,name="folder"),
    path("create_folder_home/",views.create_folder_home,name="create_folder_home"),
    path("create_folder/<str:id>/",views.create_folder,name="create_folder"),
]


urlpatterns += staticfiles_urlpatterns()