from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class pyrl_company(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.TextField()
    company_phone = models.IntegerField()
    company_email_base = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos')
    package_scheme = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.company_name}'



class pyrl_users(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=200, verbose_name="password")