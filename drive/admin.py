from django.contrib import admin
from . import models
# Register your models here.
class FolderAdmin(admin.ModelAdmin):
    model = models.Folder
    list_display = ['name', 'parent','user']

admin.site.register(models.Folder,FolderAdmin)

class FileAdmin(admin.ModelAdmin):
    model = models.File
    list_display = ['name']

admin.site.register(models.File,FileAdmin)
