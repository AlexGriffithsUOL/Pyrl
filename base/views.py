from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from utils.views import message_manager


class page_view(View):
    context = {}

    def update_context(self, key, val):
        self.context[key] = val

    def add_to_context(self, *args, **kwargs):
        for arg in args:
            for key, val in arg.items():
                self.update_context(key, val)

    def get(self, request, *args, **kwargs):
        self.add_to_context(kwargs)
        pass

    def __init__(self, *args, **kwargs):
        pass

class index(page_view):
    page_title = "Home"
    page_description = "Home page"
    page_keywords = "Home"
    template = "base/home/index.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Our page has been updated! Scroll down to see more!', length_of_time=3)
        return render(request, self.template, self.context)
    
class pricing(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Pricing"
        self.page_description = "Pricing page"
        self.page_keywords = "pricing"
        self.template = "base/pricing/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )

class about(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "About"
        self.page_description = "About page"
        self.page_keywords = "about"
        self.template = "base/about/index.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
class contact(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Contact"
        self.page_description = "Contact page"
        self.page_keywords = "contact"
        self.template = "base/contact/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
class financial_product(page_view):
    page_title = "Finance & Accountancy Solution"
    page_description = "Finance Management Product page"
    page_keywords = "Finance"
    template = "base/product_info/financial.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Welcome to our new Finance and Accountancy Solution!', length_of_time=3)
        return render(request, self.template, self.context)
    
class project_product(page_view):
    page_title = "Project Planning & Management Solution"
    page_description = "Project Planing Management Product page"
    page_keywords = "Project"
    template = "base/product_info/project_planning.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Welcome to our new Project Planning and Management Solution!', length_of_time=3)
        return render(request, self.template, self.context)
    
class communication_product(page_view):
    page_title = "Communication Solution"
    page_description = "Communication Product page"
    page_keywords = "CommunicationFinance"
    template = "base/product_info/communication.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Welcome to our new Communication Management Solution!', length_of_time=3)
        return render(request, self.template, self.context)
    
class stock_product(page_view):
    page_title = "Stock Management Solution"
    page_description = "Stock Management Product page"
    page_keywords = "STock"
    template = "base/product_info/stock.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        message_manager.attach_message(request, message_manager.STATUS.INFO, 'Welcome to our new Stock Management Solution!', length_of_time=3)
        return render(request, self.template, self.context)