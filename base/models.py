from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import TextInput
from datetime import datetime

# Create your models here.

class abstract_auditing(models.Model):
    '''Abstract class to add auditing data'''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.IntegerField(default=1)
    last_updated_at = models.DateTimeField(null=True)
    last_updated_by = models.IntegerField(null=True)

    

class company(abstract_auditing):
    class Meta:
        abstract = False
        db_table = 'company'
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
