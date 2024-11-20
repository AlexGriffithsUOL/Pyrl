from django.shortcuts import render, redirect
from uuid import uuid4
from django.views.generic import View
from .forms import RootLoginForm, FullSignupForm
from django.contrib.auth import authenticate, logout
from django.contrib import auth
from django.template.loader import render_to_string
from utils.views import retrieve_message, message_manager
from base.views import PageView

# Create your views here.
class SignUpView(PageView):
    page_title = "Signup"
    page_description = "Signup page"
    page_keywords = "Signup"
    template = "user_management/signup/index.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        self.add_to_context(form=FullSignupForm())
        return render(request, self.template, self.context)

class LoginView(PageView):
    page_title = "Login"
    page_description = "Login page"
    page_keywords = "login"
    template = "user_management/login/login.html"

    def get(self, request):
        self.add_to_context(form=RootLoginForm())
        return render(request, self.template, self.context)
        
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        User = authenticate(request, email=email, password=password)

        if User is not None:
            auth.login(request, User)
            if request.user.is_authenticated:
                if ((request.user.is_root) or (request.user.is_client_admin)):
                    return redirect("user_management:admin_dashboard")
                else:
                    return render(request, "main_app/dashboard.html", {})
            else: 
                return redirect('user_management:login')
        else:
            message_manager.attach_message(request, message_manager.STATUS.ERROR, 'Login failed, please try again!')
            return redirect('user_management:login')
        
def logout_func(request):
    logout(request=request)
    return redirect('base:index')

class AdminDashboardView(PageView):
    page_title = "Admin Dashboard"
    page_description = "Admin dashboard page"
    page_keywords = "Admin Dashboard"
    template = "user_management/root_admin/admin_dashboard.html"
    
    def get(self, request):
        super().get(
            request=request, 
            page_title=self.page_title,
            )
        
        return render(request, self.template, self.context)
    

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