from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class index(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Redirects"
        self.page_description = "Redirect"
        self.page_keywords = "Redirect"
        self.template = "inter/redir.html"
        super().__init__()


    def get(self, request):
        return redirect('base:index')