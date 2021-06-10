from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import User,Direccion


# Register your models here.
admin.site.register(User)
admin.site.register(Direccion)