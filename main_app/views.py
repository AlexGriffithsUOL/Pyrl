from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required

# Create your views here.

class dashboard(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Dashboard"
        self.page_description = "Users dashboard page"
        self.page_keywords = "Dashboard"
        self.template = "main_app/dashboard.html"
        super().__init__()

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template, 
                        { 'page_title' : self.page_title }
                        )
        else:
            return redirect('base:index')
    
class settings_view(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Settings"
        self.page_description = "Users settings page"
        self.page_keywords = "Settings"
        self.template = "main_app/settings/index.html"
        super().__init__()

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template, 
                        { 'page_title' : self.page_title }
                        )
        else:
            return redirect('base:index')
