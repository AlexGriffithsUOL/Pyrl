from django.db import models
from base.models import AbstractAuditing, PyrlClient
from customers.models import Customer

# Create your models here.

class Project(AbstractAuditing):
    class Meta:
        abstract = False
        db_table = 'project'
        
    project_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE)
    project_name = models.TextField()
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)