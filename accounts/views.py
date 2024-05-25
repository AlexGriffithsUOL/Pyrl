from django.shortcuts import render
from django.views.generic import View
from user_management.models import PyrlUser
from django.http import HttpResponse

# Create your views here.
class login(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "login"
        self.page_description = "Login page"
        self.page_keywords = "login"
        self.template = "registration/login.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
class register(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "register"
        self.page_description = "register page"
        self.page_keywords = "register"
        self.template = "registration/register.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )
    
def create(request):
    print(dir(request))
    print(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        new_user = pyrl_user(first_name=first_name, last_name=last_name, password=password)
        new_user.save()
        success = "Profile created successfully using ajax"
        return HttpResponse(success)