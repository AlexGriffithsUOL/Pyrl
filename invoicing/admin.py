from django.contrib import admin
from . models import note, invoice, invoice_product_link, terms_conditions

# Register your models here.
admin.site.register(note)
admin.site.register(invoice)
admin.site.register(invoice_product_link)
admin.site.register(terms_conditions)