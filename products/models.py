from django.db import models

from django.forms import TextInput
# Create your models here.

class pyrl_product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images')
    product_category = models.CharField(max_length=100)



    def __str__(self):
        return f'{self.product_name}'