from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class index(View):
    def __init__(self, *args, **kwargs):
        self.page_title = "Index"
        self.page_description = "Index page"
        self.page_keywords = "index"
        self.template = "base/index.html"
        super().__init__()


    def get(self, request):
        return render(request, self.template, {})