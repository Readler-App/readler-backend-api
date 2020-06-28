from django.contrib import admin
from cuser.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
