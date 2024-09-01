from django.shortcuts import render, redirect
from django.views.generic import View
from .models import product
from base.models import company
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import pytz
from uuid import uuid4

class view_products(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Your Products"
        self.page_description = "The products you have created"
        self.page_keywords = "Products"
        self.template = "main_app/products/index.html"
        super().__init__()


    def get(self, request):
        if request.user.is_authenticated:
            products = product.objects.values('pid', 'name')
            
            return render(
                request, 
                self.template,          
                { 
                    'page_title' : self.page_title,
                    'products': products,
                }
            )
        else:
            return redirect('base:index')
    
    def post(self,request):
        return render(request, self.template, {})
    
def product_info(request):
    if request.user.is_authenticated:
        fragment = "fragments/products/info_modal.html"
        product_id = request.GET.get('product_id')
        if request.is_ajax:
            information = product.objects.get(pk=product_id)
            return render(request, fragment, { 'product':information })

def new_product(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            fragment = "fragments/products/create_new_product.html"
            return render(request, fragment, {'pid':uuid4()})
    else: 
        return redirect('base:index')
    
def create(request):
    if request.user.is_authenticated:
        user_company = get_object_or_404(company, id=request.user.company_id)
        current_time = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}+00'
        if request.method == "POST":
            saving_product = product(
                company_id = user_company,
                name = request.POST.get('product_name'),
                description = request.POST.get('product_description'),
                invoice_description = request.POST.get('product_description'),
                price = float(request.POST.get('product_price')),
                image = request.POST.get('product_name'),
                category = request.POST.get('product_category'),
                created_by = request.user.id,
                created_at = current_time,
                last_updated_by = request.user.id,
                last_updated_at = current_time
                )
            
            saving_product.save()
        else:
            print('failed')
        return HttpResponse("Piss yourself uncs")
    else:
        return redirect('base:index')
    
def delete(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = request.POST['product_id']
            specific_product = product.objects.get(pid=product_id)
            specific_product.delete()
            return HttpResponse("deleted")
        