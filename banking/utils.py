from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.link_token_account_filters import LinkTokenAccountFilters
from plaid.model.depository_filter import DepositoryFilter
from plaid.model.depository_account_subtypes import DepositoryAccountSubtypes
from plaid.model.depository_account_subtype import DepositoryAccountSubtype
from plaid.model.credit_filter import CreditFilter
from plaid.model.credit_account_subtypes import CreditAccountSubtypes
from plaid.model.credit_account_subtype import CreditAccountSubtype
from plaid.model.country_code import CountryCode
from plaid.model.link_token_transactions import LinkTokenTransactions
from plaid import Configuration, ApiClient
import os
from django.conf import settings
from customers.models import Customer
from transaction.webhooks import build_webhook

# ENDPOINTS = {
#     'Production': 'https://production.plaid.com',
#     'Sandbox': 'https://sandbox.plaid.com'
# }

def get_plaid_client():
    configuration = Configuration(
        host=settings.PLAID_API_URL,
        api_key={
            'clientId': settings.PLAID_CLIENT_ID,
            'secret': settings.PLAID_API_KEY
        }
    )

    api_client = ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)
    return client

def get_link_token(customer: Customer):
    client = get_plaid_client()

    user = LinkTokenCreateRequestUser(
        client_user_id=f'pyrl-{str(customer.customer_uuid)}',
        phone_number='07701028269'
    )
    
    product_list = [
        Products('transactions')
    ]
    
    transactions=LinkTokenTransactions(days_requested=730)
    country_codes=[CountryCode('GB')]
    #   redirect_uri='https://domainname.com/oauth-page.html',
    account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=DepositoryAccountSubtypes([
                    DepositoryAccountSubtype('checking'),
                    DepositoryAccountSubtype('savings')
                ])
            ),
            credit=CreditFilter(
                account_subtypes=CreditAccountSubtypes([
                    CreditAccountSubtype('credit card')
                ])
            )
    )
    
    link_token_data = {
        'user': user,
        'client_name': 'Pyrl UK',
        'products': product_list,
        'country_codes': country_codes,
        'transactions': transactions,
        'language': 'en',
        'account_filters': account_filters,
        'webhook': build_webhook(customer.customer_id)
    }
    
    request = LinkTokenCreateRequest(
        **link_token_data
    )
    public_token = client.link_token_create(request)
    return public_token.link_token