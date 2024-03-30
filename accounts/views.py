from django.shortcuts import render
from django.views.generic import View

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