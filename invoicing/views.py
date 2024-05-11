from django.shortcuts import render
from django.views import View
from invoicing.models import invoice
from django.contrib.auth.models import User
# Create your views here.
class index(View):
    def get(self, request):
        total_invoices = invoice.objects.all()
        selected_invoice = total_invoices[0]
        print(User.objects.all())
        print(dir(selected_invoice))
        print(selected_invoice.pid)
        print(selected_invoice.invoice_id)
        print(selected_invoice.company_id)
        print(selected_invoice.date_of_invoice)
        return render(request, 'invoice/index.html', {'total_invoices': total_invoices, 'selected_invoice': selected_invoice})