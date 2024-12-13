from django.shortcuts import render
from base.views import PageView
# Create your views here.

class index(PageView):
    template = 'main_app/customers/index.html'
    page_title = 'customesr'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        customer = range(0, 20)
        self.context['customer'] = customer
        return render(request, self.template, self.context)
