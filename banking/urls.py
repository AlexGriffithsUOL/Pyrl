from django.urls import path
from . import views

app_name='banking'

urlpatterns = [
    path('<int:customer_id>/link/', view=views.PlaidGetLink.as_view(), name='banking-link'),
    path('<int:customer_id>/public_token', view=views.PlaidSaveLinkInfo.as_view(), name='public-token'),
    path('<str:bank_account_id>/details/', view=views.BankDetailsView.as_view(), name='bank-details')
]