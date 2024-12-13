from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from uuid import uuid4
import random
from invoicing.models import invoice, invoice_product_link, product
from .forms import row_form
from base.views import PageView

# Create your views here.
class InvoicingMainView(PageView):
    page_title = 'Invoice'
    template = 'main_app/invoice/index.html'
    
class InvoicingCreateInvoiceView(PageView):
    page_title = 'Create Invoice'
    template = 'main_app/invoice/create.html'
    
    
def get_row(request, fragment_id):
    if request.user.is_authenticated:
        fragment = "fragments/invoice/row.html"
        user_products = product.objects.all()
        form = row_form()
        return render(request, fragment, 
                      {
                      'product_choices':user_products, 
                      'form': form 
                      })