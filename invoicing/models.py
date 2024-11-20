from django.db import models
from products.models import product
from base.models import PyrlClient
from base.models import AbstractAuditing
from datetime import datetime, date
from uuid import uuid4

# Create your models here.
class terms_conditions(AbstractAuditing):
    class Meta:
        abstract = False
        db_table = 'terms_and_conditions'

    pid = models.BigAutoField(primary_key=True)
    terms = models.TextField(null=False, blank=False)

class note(AbstractAuditing):
    class Meta:
        abstract = False
        db_table = 'note'

    pid = models.BigAutoField(primary_key=True)
    note = models.TextField(null=False, blank=False)

class invoice(AbstractAuditing):
    class Meta:
        abstract = False
        db_table = 'invoice'
    
    pid = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid4, editable=False)
    description = models.TextField(default=f'Invoice eee to Alex' , max_length=40, null=False, blank=False)
    client_id = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE, null=False, blank=False)
    due_date = models.DateField(null=True, blank=False)
    note = models.ForeignKey(to=note, on_delete=models.CASCADE, null=True, blank=False)
    terms_conditions = models.ForeignKey(to=terms_conditions, on_delete=models.CASCADE, null=True, blank=False)
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, null=True, blank=True)
    paid = models.BooleanField(default=False)

class invoice_product_link(models.Model):
    class Meta:
        db_table = 'invoice_product_link'

    pid = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(to=product, on_delete=models.CASCADE, null=False, blank=False)
    invoice_id = models.ForeignKey(to=invoice, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.DecimalField(default=0.0, max_digits=10, decimal_places=3, null=False, blank=False)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=3, null=False, blank=False)