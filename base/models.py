from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import TextInput
from datetime import datetime

# Create your models here.

class AbstractAuditingFields():
    CREATED_AT = models.DateTimeField(default=datetime.now)
    CREATED_BY = models.IntegerField(default=1)
    LAST_UPDATED_AT = models.DateTimeField(null=True)
    LAST_UPDATED_BY = models.IntegerField(null=True)

class AbstractAuditing(models.Model):
    '''Abstract class to add auditing data'''

    class Meta:
        abstract = True

    created_at = AbstractAuditingFields.CREATED_AT
    created_by = AbstractAuditingFields.CREATED_BY
    last_updated_at = AbstractAuditingFields.LAST_UPDATED_AT
    last_updated_by = AbstractAuditingFields.LAST_UPDATED_BY



class company(AbstractAuditing):
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
