from django.db import models
from django.forms import TextInput
from base.models import company, abstract_auditing
# Create your models here.

class product(abstract_auditing):
    class Meta:
        db_table = 'product'
        abstract = False

    pid = models.BigAutoField(primary_key=True)
    company_id = models.ForeignKey(to=company, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    invoice_description = models.TextField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)
    image = models.ImageField(upload_to='static/product_images')
    category = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return f'{self.name}'