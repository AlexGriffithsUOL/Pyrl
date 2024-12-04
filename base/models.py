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
    
class PyrlModel(models.Model):
    class Meta:
        abstract = True
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    read_only_attributes = { 'created_by', 'created_at' }
    
    def _read_only_check(self, attribute):
        if attribute in self.read_only_attributes:
            return True
    
    def is_read_only(self, attribute):
        self._read_only_check(attribute)
        
    
class PyrlClient(PyrlModel):
    class Meta:
        abstract = False
        db_table = 'client'
        
    client_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    telephone_number = models.CharField(max_length=9)
    email_base = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    domain = models.TextField(null=True)
    logo = models.ImageField(upload_to='client_logos')
    package_scheme = models.CharField(max_length=1)
    created_at = AbstractAuditingFields.CREATED_AT

    def __str__(self):
        return f'{self.client_name}'
