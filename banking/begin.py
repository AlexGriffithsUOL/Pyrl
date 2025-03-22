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

PLAID_CLIENT_ID='679fb4ba99e8220024b9616e'
PLAID_TEST_KEY='19f259a1fe29ff0b53c6e15eb990cd'


ENDPOINTS = {
    'Production': 'https://production.plaid.com',
    'Sandbox': 'https://sandbox.plaid.com'
}

def get_plaid_client():
    configuration = Configuration(
        host=ENDPOINTS['Sandbox'],
        api_key={
            'clientId': PLAID_CLIENT_ID,
            'secret': PLAID_TEST_KEY
        }
    )

    api_client = ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)
    return client

def get_link_token():
    # Configure Plaid API Client
    configuration = Configuration(
        host=ENDPOINTS['Sandbox'],
        api_key={
            'clientId': PLAID_CLIENT_ID,
            'secret': PLAID_TEST_KEY
        }
    )

    api_client = ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    request = LinkTokenCreateRequest(
        user=LinkTokenCreateRequestUser(
            client_user_id='user-id',
            phone_number='+1 415 5550123'
        ),
        client_name='Personal Finance App',
        products=[Products('transactions')],
        transactions=LinkTokenTransactions(
            days_requested=730
        ),
        country_codes=[CountryCode('US')],
        language='en',
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
    )
    # create link token
    # from plaid.models.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
    from plaid.models import ItemPublicTokenExchangeRequest
    public_token = client.link_token_create(request)
    print(public_token.link_token)
    # request = ItemPublicTokenExchangeRequest(public_token=public_token.link_token)

    # response = client.item_public_token_exchange(request)
    # access_token = response['access_token']
    # item_id = response['item_id']
    # link_token = response['link_token']
    return public_token.link_token