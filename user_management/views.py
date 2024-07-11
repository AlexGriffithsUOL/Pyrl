from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm, RootLoginForm, FullSignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, user_logged_in, user_logged_out
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
class signup(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "user_management/signup/test.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title,
                        'form': FullSignupForm() }
                      )
    
class login(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Login"
        self.page_description = "Login page"
        self.page_keywords = "login"
        self.template = "user_management/login/subuser_login.html"
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
        self.template = "user_management/login/root_login.html"
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
        email = request.POST['email']
        password = request.POST['password']
        User = authenticate(request, email=email, password=password)
        # User.authenticate(email=username, password=password)

        if User is not None:
            auth.login(request, User)
            if request.user.is_authenticated:
                return redirect('main_app:index')#User to the dashboard!)
            else: 
                return redirect('user_management:login_root')
        else:
            print(request, "invalid credentials")
            return redirect('user_management:login_root')
        
def logout_func(request):
    logout(request=request)
    return redirect('base:index')

class change_password(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "user_management/change_password/change_password.html"
        super().__init__()

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template, 
                        { 'page_title' : self.page_title }
                        )
        else:
            return redirect('base:index')

class forgot_password(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "user_management/login/forgot_password.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
