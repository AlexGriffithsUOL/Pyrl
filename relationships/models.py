from django.db import models
from django.contrib import admin
from base.models import AbstractAuditing, AbstractAuditingFields

# Create your models here.
class EntityTypes(models.Model):
    class Meta:
        abstract = False
        db_table = 'legal_entity'
    
    entity_id = models.CharField(max_length=3, unique=True, editable=False)
    description = models.TextField(null=False)

class Relationship(AbstractAuditing):
    class Meta:
        abstract = False
        db_table = 'relationship'
        
    relationship_id = models.BigAutoField(primary_key=True)
    display_name = models.TextField()
    legal_entity = models.ForeignKey(to=EntityTypes, to_field='entity_id', on_delete=models.CASCADE)
    