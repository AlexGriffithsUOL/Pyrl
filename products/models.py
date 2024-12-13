from django.db import models
from django.forms import TextInput
from base.models import PyrlClient, AbstractAuditing, AbstractAuditingFields
# Create your models here.

class product(AbstractAuditing):
    class Meta:
        db_table = 'product'
        abstract = False

    product_id = models.BigAutoField(primary_key=True)
    client_id = models.ForeignKey(to=PyrlClient, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    product_description = models.TextField()
    invoice_description = models.TextField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)
    image = models.ImageField(upload_to='static/product_images')
    category = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return f'{self.name}'
    
class BasePyrlModel(models.Model):
    class Meta:
        abstract = True

    class functions:
        def insert_update(*args, **kwargs):
            raise NotImplementedError('This method has not been implemented, replace with "pass" if not necessary')

        

class ProductCategory(models.Model):
    class Meta:
        db_table = 'product_category'

    product_category_id = models.BigAutoField(primary_key=True)
    category_description = models.TextField()
    product_category_value = models.TextField(max_length=4, blank=True, default='CAT')
    client_id = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE, null=False, blank=False)
    created_at = AbstractAuditingFields.CREATED_AT
    created_by = AbstractAuditingFields.CREATED_BY
    last_updated_at = AbstractAuditingFields.LAST_UPDATED_AT
    last_updated_by = AbstractAuditingFields.LAST_UPDATED_BY


