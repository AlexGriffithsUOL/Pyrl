from django.contrib import admin
from .models import pyrl_user, pyrl_company

# Register your models here.
admin.site.register(pyrl_user)
admin.site.register(pyrl_company)