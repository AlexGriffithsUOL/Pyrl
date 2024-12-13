from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import product, ProductCategory
from base.models import PyrlClient
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from uuid import uuid4
from base.views import PageView
from core.decorators.function_decorators import ajax_required

class ProductMainView(PageView):
    page_title = "Your Products"
    page_description = "The products you have created"
    page_keywords = "Products"
    template = "main_app/products/index.html"

    def get(self, request):
        if request.user.is_authenticated:
            products = product.objects.values('product_id', 'name')
            self.add_to_context(products=products)
            return super().get(request)
        else:
            return redirect('four')
    
    def post(self,request):
        return render(request, self.template, {})
    
class ProductCategoriesView(PageView):
    page_title = 'Product Categories'
    page_description = 'User defined product categories'
    page_keywords ='Product Categories'
    template = 'main_app/products/product_categories.html'

    def get(self, request):
        product_categories = ProductCategory.objects.filter(client_id=request.user.client_id)
        self.add_to_context(product_categories=product_categories)
        return super().get(request)
    
@login_required
@ajax_required
def AsyncGetProductInfo(request):
    fragment = "fragments/products/info_modal.html"
    product_id = request.GET.get('product_id')
    product_categories = ProductCategory.objects.filter(client_id=request.user.client_id)
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
@ajax_required
def AsyncGetCreateNewProductHTMLFunc(request):
    if request.method == 'GET':
        fragment = "fragments/products/create_new_product.html"
        product_categories = ProductCategory.objects.filter(client_id=request.user.client_id)
        return render(
            request, 
            fragment, 
            {
                'product_id': uuid4(),
                'product_categories': product_categories
            }
        )
    
@login_required
@ajax_required
def AsyncCreateProduct(request):
    parent_client = get_object_or_404(PyrlClient, client_id=request.user.client_id)
    current_time = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}+00'
    
    if request.method == "POST":
        saving_product = product(
            client_id = parent_client,
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
        
        saving_product.save()
        
    return HttpResponse(200)
    
@login_required
@ajax_required
def AsyncDeleteProduct(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        specific_product = product.objects.get(product_id=product_id)
        specific_product.delete()
        return HttpResponse(200)
        
@login_required
@ajax_required
def AsyncEditProduct(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        specific_product = product.objects.get(product_id=product_id)
        specific_product.name = request.POST['name']
        specific_product.description = request.POST['description']
        specific_product.price = request.POST['price']
        specific_product.category = request.POST['category']
        specific_product.save()
        return HttpResponse(200)