from django.db import models
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



class PyrlClient(models.Model):
    class Meta:
        abstract = False
        db_table = 'client'
    id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)
    client_description = models.TextField()
    client_phone = models.CharField(max_length=9)
    client_email_base = models.CharField(max_length=100)
    client_website = models.CharField(max_length=100)
    client_logo = models.ImageField(upload_to='client_logos')
    package_scheme = models.CharField(max_length=1)
    created_at = AbstractAuditingFields.CREATED_AT

    def __str__(self):
        return f'{self.client_name}'
