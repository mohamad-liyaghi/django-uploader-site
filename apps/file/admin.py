from django.contrib import admin
from .models import UserFile,IpAddress 
# Register your models here.
admin.site.register(UserFile)
admin.site.register(IpAddress)