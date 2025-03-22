from django.db import models
from django.contrib import admin
from base.models import AbstractAuditing, AbstractAuditingFields, PyrlClient
from base.utils.model_mixins import SoftDeleteMixin
import uuid

# Create your models here.
class EntityTypes(models.Model):
    class Meta:
        abstract = False
        db_table = 'legal_entity'
    
    entity_id = models.CharField(max_length=3, unique=True, editable=False)
    description = models.TextField(null=False)
    
    def __str__(self):
        return f'{self.entity_id} - {self.description}'    

class Customer(AbstractAuditing, SoftDeleteMixin):
    class Meta:
        abstract = False
        db_table = 'customer'
        
    customer_id = models.BigAutoField(primary_key=True)
    display_name = models.TextField()
    legal_entity = models.ForeignKey(to=EntityTypes, to_field='entity_id', on_delete=models.CASCADE)
    plaid_access_token = models.TextField(null=True, blank=True)
    client = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE)
    customer_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return f'{self.customer_id} - {self.display_name} / {self.legal_entity}'
    
class CustomerGroup(AbstractAuditing, SoftDeleteMixin):
    class Meta:
        db_table = 'customer_group'
        abstract = False
        
    customer_group_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    client = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE)

class CustomerGroupCustomerLink(AbstractAuditing):
    class Meta:
        db_table = 'customer_group_customer_link'
        abstract = False
        
    customer_group_customer_group_id = models.BigAutoField(primary_key=True)
    customer_group = models.ForeignKey(to=CustomerGroup, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    
class CustomerContact(AbstractAuditing, SoftDeleteMixin):
    class Meta:
        db_table = 'customer_contact'
        abstract = False
        
    customer_contact_id = models.BigAutoField(primary_key=True)
    forename = models.TextField()
    surname = models.TextField()
    date_of_birth = models.DateField()
    email_address = models.EmailField()
    activated = models.BooleanField(default=False)
    customer_contact_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        self.activated = False
        super().delete()
        
        
    
    