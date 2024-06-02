from django.shortcuts import render, redirect
from django.views.generic import View
from .models import pyrl_product
import math
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class view_products(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Your Products"
        self.page_description = "The products you have created"
        self.page_keywords = "Products"
        self.template = "main_app/products/index.html"
        super().__init__()


    def get(self, request):
        if request.user.is_authenticated:
            self.products = pyrl_product.objects.all()
            return render(
                request, 
                self.template,          
                { 
                    'page_title' : self.page_title,
                    'products': self.products,
                }
            )
        else:
            return redirect('base:index')

def test(request):
    if request.user.is_authenticated:
        print(request.POST)
        print(request.GET)

        if request.method == 'GET':
            fragment = "fragments/products/test_modal.html"
            return render(request, fragment, {})
    else: 
        return redirect('base:index')
    
def create(request):
    if request.user.is_authenticated:
        product_name = request.POST.get('product_name')
        product_brand = request.POST.get('product_brand')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_category = request.POST.get('product_category')
        print(product_name)
        print(product_brand)
        print(product_description)
        print(product_price)
        print(product_category)

        product = pyrl_product(
            product_name=product_name, 
            product_description=product_description, 
            product_price=product_price, 
            product_category=product_brand
            )
        
        product.save()
        return HttpResponse("Piss yourself uncs")
    else:
        return redirect('base:index')