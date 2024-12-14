from django.shortcuts import render, redirect
from django.views.generic import View
from base.views import PageView

# Create your views here.

class index(PageView):
    def __init__(self, *args, **kwargs):
        self.page_title = "Redirects"
        self.page_description = "Redirect"
        self.page_keywords = "Redirect"
        self.template = "inter/redir.html"
        super().__init__()


    def get(self, request):
        return redirect('base:index')

class FourOhFourView(PageView):
    page_title = "404"
    page_description = "404"
    page_keywords = "404"
    template = "404.html"

    def get(self, request):
        return super().get(request)
    
class maintenance(PageView):
    page_title = "Maintenance"
    page_description = "Maintenance page"
    page_keywords = "Maintenance"
    template = "maintenance.html"

    def get(self, request):
        super().get(request=request, page_title = self.page_title)
        return render(request, self.template, self.context)