from base.views import WebhookView
from customers.models import Customer
from django.http import JsonResponse
from base.mixins import CsrfExemptMixin
from django.conf import settings
from base.helpers import build_base_url

def build_webhook(customer_id):
    client = Customer.objects.get(customer_id=customer_id).client
    return f'{build_base_url(client.client_id)}/app/transaction/webhooks/transaction-update/{customer_id}/'

class TransactionUpdateView(CsrfExemptMixin, WebhookView):
        
    def post(self, request, customer_id, *args, **kwargs):
        try:
            print(request.POST.dict())
            customer = Customer.objects.get(customer_id=customer_id)
            return JsonResponse({
                'status':'success'
                })
        except Exception as err:
            print(err)
            return JsonResponse({
                'status':'error',
                'message': 'Error finding customer'
                })