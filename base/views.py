from django.shortcuts import render, redirect
from django.views.generic import View
from .mixins import UserAuthenticatedMixin

class PageView(View):
    context = {}
    
    def update_context(self, key, val):
        self.context[key] = val

    def add_to_context(self, *args, **kwargs):
        for arg in args:
            for key, val in arg.items():
                self.update_context(key, val)
                
        for key, val in kwargs.items():
            self.update_context(key,val)
            
    def get_page_attrs(self):
        if hasattr(self, 'page_title'): self.add_to_context(page_title=self.page_title) 

    def get(self, request, *args, **kwargs):
        self.add_to_context(**kwargs)
        self.get_page_attrs()
        return render(request=request, template_name=self.template, context=self.context)
    
    def post(self, request, *args, **kwargs):
        self.add_to_context(**kwargs)
        self.get_page_attrs()
        return render(request=request, template_name=self.template, context=self.context)

    def __init__(self, request=None, *args, **kwargs):
        self.add_to_context(*args, **kwargs)

class WebhookView(View):
    def post(self, request, *args, **kwargs):
        raise Exception('Webhook view post has not been implemented')
        
    
class AuthenticatedView(UserAuthenticatedMixin, PageView):
    pass

class HomePageMainView(PageView):
    page_title = "Home"
    page_description = "Home page"
    page_keywords = "Home"
    template = "base/home/index.html"
    
class HomePagePricingView(PageView):
    page_title = "Pricing"
    page_description = "Pricing page"
    page_keywords = "pricing"
    template = "base/pricing/index.html"

class HomePageAboutView(PageView):
    page_title = "About"
    page_description = "About page"
    page_keywords = "about"
    template = "base/about/index.html"
    
class HomePageContactView(PageView):
    page_title = "Contact"
    page_description = "Contact page"
    page_keywords = "contact"
    template = "base/contact/index.html"
    
class HomePageFinancialProductView(PageView):
    page_title = "Finance & Accountancy Solution"
    page_description = "Finance Management Product page"
    page_keywords = "Finance"
    template = "base/product_info/financial.html"
    
class HomePageProjectProductView(PageView):
    page_title = "Project Planning & Management Solution"
    page_description = "Project Planing Management Product page"
    page_keywords = "Project"
    template = "base/product_info/project_planning.html"
    
class HomePageCommunicationProductView(PageView):
    page_title = "Communication Solution"
    page_description = "Communication Product page"
    page_keywords = "CommunicationFinance"
    template = "base/product_info/communication.html"
    
class HomePageStockProductView(PageView):
    page_title = "Stock Management Solution"
    page_description = "Stock Management Product page"
    page_keywords = "STock"
    template = "base/product_info/stock.html"
    