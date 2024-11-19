from django.shortcuts import render, redirect
from django.views.generic import View
from .models import product, ProductCategory
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

    @login_required
    def get(self, request):
        products = product.objects.values('product_id', 'name')

        return render(
            request, 
            self.template,          
            { 
                'page_title': self.page_title,
                'products': products
            }
        )
    
    def post(self,request):
        return render(request, self.template, {})
    
@login_required
def product_info(request):
    fragment = "fragments/products/info_modal.html"
    product_id = request.GET.get('product_id')
    product_categories = ProductCategory.objects.filter(company_id=request.user.company_id)
    if request.is_ajax:
        information = product.objects.get(pk=product_id)
        return render(
            request, 
            fragment, 
            { 
                'product': information,
                'product_categories': product_categories 
            }
        )

@login_required
def new_product(request):
    if request.method == 'GET':
        fragment = "fragments/products/create_new_product.html"
        product_categories = ProductCategory.objects.filter(company_id=request.user.company_id)
        return render(
            request, 
            fragment, 
            {
                'product_id': uuid4(),
                'product_categories': product_categories
            }
        )
    
@login_required
def create(request):
    user_company = get_object_or_404(company, id=request.user.company_id)
    current_time = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}+00'
    if request.method == "POST":
        saving_product = product(
            company_id = user_company,
            name = request.POST.get('product_name'),
            product_description = request.POST.get('product_description'),
            invoice_description = request.POST.get('product_description'),
            price = float(request.POST.get('product_price')),
            image = request.POST.get('product_name'),
            category = request.POST.get('product_category'),
            created_by = request.user.id,
            created_at = current_time,
            last_updated_by = request.user.id,
            last_updated_at = current_time
            )
        
        print(saving_product.category)
        
        saving_product.save()
    return HttpResponse("Piss yourself uncs")
    
@login_required
def delete(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        specific_product = product.objects.get(product_id=product_id)
        specific_product.delete()
        return HttpResponse("deleted")
        
@login_required
def edit(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        specific_product = product.objects.get(product_id=product_id)
        specific_product.name = request.POST['name']
        specific_product.description = request.POST['description']
        specific_product.price = request.POST['price']
        specific_product.category = request.POST['category']
        specific_product.save()
        return HttpResponse(200)