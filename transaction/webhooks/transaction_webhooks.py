from django.urls import path, include
from . import webhook_views

transaction_webhook_url_patterns = [
    path('transaction-update/<str:customer_id>/', view=webhook_views.TransactionUpdateView.as_view(), name='transaction-update')
]

urlpatterns = transaction_webhook_url_patterns