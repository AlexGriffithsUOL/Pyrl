from django.db import models
from datetime import datetime

# Create your models here.

class AbstractAuditingFields():
    CREATED_AT = models.DateTimeField(default=datetime.now)
    CREATED_BY = models.IntegerField(default=1)
    LAST_UPDATED_AT = models.DateTimeField(null=True)
    LAST_UPDATED_BY = models.IntegerField(null=True)

class AbstractAuditingCreated(models.Model):
    '''Abstract class to add created_by and created_at'''
    class Meta:
        abstract = True
        
    created_at = AbstractAuditingFields.CREATED_AT
    created_by = AbstractAuditingFields.CREATED_BY
    
class AbstractAuditingLastUpdate(models.Model):
    '''Abstract class to add last_updated_by and last_updated_at'''
    class Meta:
        abstract = True
        
    last_updated_at = AbstractAuditingFields.LAST_UPDATED_AT
    last_updated_by = AbstractAuditingFields.LAST_UPDATED_BY
    

class AbstractAuditing(AbstractAuditingCreated, AbstractAuditingLastUpdate):
    '''Abstract class to add auditing data'''

    class Meta:
        abstract = True
    
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
    
class PyrlAuditModel(PyrlModel, AbstractAuditing):
    class Meta:
        abstract = True
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
class PyrlClient(PyrlModel):
    class Meta:
        abstract = False
        db_table = 'client'
        
    client_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    telephone_number = models.CharField(max_length=9)
    email_base = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    domain = models.TextField(null=True)
    logo = models.ImageField(upload_to='client_logos', null=True)
    package_scheme = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.client_name}'
