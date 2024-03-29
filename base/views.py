from django.shortcuts import render
from django.views.generic import View
from .forms import SignUpForm

# Create your views here.
class PyrlBaseView(View):
    def __init__(self, *args, **kwargs):
        self.page_title = kwargs.pop('page_title')
        self.page_description = kwargs.pop('page_description')
        self.page_keywords = kwargs.pop('page_keywords')
        self.template = kwargs.pop('template')
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )

class index(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Home"
        self.page_description = "Home page"
        self.page_keywords = "Home"
        self.template = "base/home/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
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
    
class form(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "base/form/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title,
                        'form': SignUpForm() }
                      )