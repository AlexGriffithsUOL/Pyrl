from django.urls import path, include
from . import views

app_name = 'transaction'

urlpatterns = [
    path('<int:customer_id>/create/', view=views.TransactionCreateView.as_view(), name='tr_create'),
    path('<int:customer_id>/ledger/', view=views.GeneralLedgerView.as_view(), name='gl'),
    path('refresh_token/', view=views.RefreshTransactions.as_view(), name='eeeehh'),
    path('webhooks/', include('transaction.webhooks'))
]