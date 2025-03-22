from django.shortcuts import render, redirect
from uuid import uuid4
from django.views.generic import View
from .forms import RootLoginForm, FullSignupForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from utils.views import message_manager
from base.views import PageView
from .models import PyrlUser


# Create your views here.
class UserManagementSignUpView(PageView):
    page_title = "Signup"
    page_description = "Signup page"
    page_keywords = "Signup"
    template = "user_management/signup/index.html"

    def get(self, request):
        self.add_to_context(form=FullSignupForm())
        return super().get(request)

class UserManagementLoginView(PageView):
    page_title = "Login"
    page_description = "Login page"
    page_keywords = "login"
    template = "user_management/login/login.html"

    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
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
                    return redirect("main_app:user_management:admin_dashboard")
                else:
                    return redirect('main_app:index')
            else: 
                return redirect('main_app:user_management:login')
        else:
            message_manager.attach_message(request, message_manager.STATUS.ERROR, 'Login failed, please try again!')
            return redirect('main_app:user_management:login')

@login_required        
def LogOutFunc(request):
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
    

class UserManagementChangePasswordView(PageView):
    page_title = "Form"
    page_description = "Form page"
    page_keywords = "form"
    template = "user_management/change_password/change_password.html"

    def get(self, request):
        if request.user.is_authenticated:
            return super().get()
        else:
            return redirect('base:index')

class UserManagementForgotPasswordView(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Form"
        self.page_description = "Form page"
        self.page_keywords = "form"
        self.template = "user_management/change_password/forgot_password.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
        
class ListUserView(PageView):
    page_title = 'Users'
    template = 'main_app/user_management/user/list.html'
    
    def get(self, request):
        users = PyrlUser.objects.filter(client=request.user.client)
        self.add_to_context(users=users)
        return render(
            request,
            self.template,
            self.context
        )
        
class CreateUserView(PageView):
    page_title = 'Create a User'
    template = 'main_app/user_management/user/create.html'
    def __init__(self, *args, **kwargs):
        super().__init__()
        
    def get(self, request):
        return