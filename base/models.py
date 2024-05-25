from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import TextInput
# Create your models here.

class pyrl_company(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.TextField()
    company_phone = models.CharField(max_length=9)
    company_email_base = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos')
    package_scheme = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.company_name}'
