from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm, RootLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    
class signup(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "base/signup/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title,
                        'form': SignUpForm() }
                      )
    
class login(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Login"
        self.page_description = "Login page"
        self.page_keywords = "login"
        self.template = "base/login/secondary_index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
class login_root(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Login"
        self.page_description = "Login page"
        self.page_keywords = "login"
        self.template = "base/login/index.html"
        super().__init__()

    def get(self, request):
        form = RootLoginForm()
        return render(request, self.template, 
                        { 
                          'page_title' : self.page_title, 
                          'form': form
                        }
                      )
        
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        User.authenticate(username=username, password=password)

        if User is not None:
            login(request, User)
            return redirect('main_app:index')#User to the dashboard!)
        else:
            print(request, "invalid credentials")
            return redirect('login')