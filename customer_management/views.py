from django.shortcuts import render
from base.views import page_view
# Create your views here.

class index(page_view):
    template = 'main_app/customers/index.html'
    page_title = 'Customers'

    def get(self, request):
        super().__init__(request=request,page_title=self.page_title)
        customers = range(0, 10)
        self.context['customers'] = customers
        return render(request, self.template, self.context)
