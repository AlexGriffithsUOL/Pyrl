from django.contrib import admin
from .models import invoice_product, invoice

# Register your models here.
admin.site.register(invoice)
admin.site.register(invoice_product)