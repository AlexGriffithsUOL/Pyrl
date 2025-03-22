from django.db import models
from customers.models import Customer


class BankInstitution(models.Model):
    class Meta:
        db_table='bank_institution'
        
    institution_id = models.TextField(primary_key=True)
    name = models.TextField()

class BankAccount(models.Model):
    class Meta:
        db_table = 'bank_account'
    bank_account_id = models.TextField(primary_key=True)
    name = models.TextField()
    mask = models.TextField()
    bank_type = models.TextField()
    bank_subtype = models.TextField()
    verification_status = models.TextField(null=True)
    class_type = models.TextField(null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    institution = models.ForeignKey(to=BankInstitution, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, default='ENA')
    