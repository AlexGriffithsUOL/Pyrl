from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class dashboard(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Dashboard"
        self.page_description = "Users dashboard page"
        self.page_keywords = "Dashboard"
        self.template = "main_app/dashboard.html"
        super().__init__()

    def get(self, request):
        return render(request, self.template, 
                      { 'page_title' : self.page_title }
                      )