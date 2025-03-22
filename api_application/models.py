from django.db import models
from base.models import PyrlClient
from hashlib import sha256

# Create your models here.
class ApiKey(models.Model):
    class Meta:
        db_table = 'api_key'
        abstract = False
        
    api_key_id = models.BigAutoField(primary_key=True)
    api_key = models.TextField(default=sha256)
    client = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        key = sha256().hexdigest()
        self.api_key = key
        super().save()