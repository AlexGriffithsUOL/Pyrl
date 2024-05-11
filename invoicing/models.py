from django.db import models
from products.models import pyrl_product
from base.models import pyrl_company
import uuid

# Create your models here.
class invoice(models.Model):
    pid = models.BigAutoField(primary_key=True, auto_created=True)
    invoice_id = models.UUIDField(default=uuid.uuid4, unique=True)
    company_id = models.ForeignKey(pyrl_company, on_delete=models.CASCADE)
    date_of_invoice = models.DateField()

class invoice_product(models.Model):
    pid = models.BigAutoField(primary_key=True, auto_created=True)
    invoice_id = models.ForeignKey(invoice, on_delete=models.CASCADE)
    product_id = models.ForeignKey(pyrl_product, on_delete=models.CASCADE)
    date_of_order = models.DateField()
    item_description = models.CharField(max_length=100)
    price_per_item = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=9, decimal_places=2)