from django.shortcuts import render
from django.views.generic import View
from .models import pyrl_product
import math

class view_products(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Home"
        self.page_description = "Home page"
        self.page_keywords = "Home"
        self.template = "products/index.html"
        super().__init__()


    def get(self, request):
        self.products = pyrl_product.objects.all()
        return render(
            request, 
            self.template,          
            { 
                'page_title' : self.page_title,
                'products': self.products,
            }
        )

# def create(request):
#     print(dir(request))
#     print(request.POST)
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']

#         new_user = pyrl_user(first_name=first_name, last_name=last_name, password=password)
#         new_user.save()
#         success = "Profile created successfully using ajax"
#         return HttpResponse(success)