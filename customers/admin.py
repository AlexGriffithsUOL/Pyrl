from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EntityTypes)
admin.site.register(Customer)
admin.site.register(CustomerGroup)
admin.site.register(CustomerGroupCustomerLink)