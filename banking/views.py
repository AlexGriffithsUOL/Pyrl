import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from base.views import PageView
from .utils import get_plaid_client, get_link_token
from customers.models import Customer
from plaid.api import plaid_api
from plaid.models import ItemPublicTokenExchangeRequest, ItemPublicTokenExchangeResponse
from plaid import Configuration, ApiClient
import os
from .models import BankInstitution, BankAccount

class PlaidGetLink(PageView):
    template='main_app/banking/link.html'
    page_title='Link your bank'
    
    def get(self, request, customer_id):
        customer = Customer.objects.get(customer_id=customer_id)
        
        if customer.plaid_access_token != None:
            return redirect('main_app:index')
        
        link_token = get_link_token(customer)
        self.add_to_context(link_token=link_token)
        self.add_to_context(customer_id=customer_id)
        return render(request, self.template, self.context)

class PlaidSaveLinkInfo(PageView):
    template='main_app/banking/link.html'
    page_title='Link your bank'
    
    def get_plaid_access_token(self, public_token):
        plaid_client = get_plaid_client()
        plaid_token_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        plaid_response = plaid_client.item_public_token_exchange(plaid_token_request)
        return plaid_response
    
    def post(self, request, customer_id):
        
        customer = Customer.objects.get(customer_id=customer_id)
        
        if customer.plaid_access_token != None:
            return redirect('main_app:customers:details', customer_id=customer_id)
        
        req = request
        data = json.loads(req.body)
        
        plaid_response = self.get_plaid_access_token(public_token=data['public_token'])

        customer.plaid_access_token = plaid_response['access_token']
        customer.save()
        metadata = data['metadata']

        try:
            institution = BankInstitution.objects.get(institution_id=metadata['institution']['institution_id'])
        except Exception as e:
            institution = BankInstitution(**metadata['institution'])
            institution.save()
            
        accounts = metadata['accounts']
        
        for account in accounts:
            try:
                bank_account = BankAccount.objects.get(bank_account_id=account['id'])
            except Exception as e:
                account['bank_account_id'] = account['id']
                account['bank_type'] = account['type']
                account['bank_subtype'] = account['subtype']
                del account['id']
                del account['type']
                del account['subtype']
                BankAccount(**account, customer=customer, institution=institution).save()
                
        return redirect('main_app:index')
    
class BankDetailsView(PageView):
    template='main_app/banking/details.html'
    page_title='Bank Details'
    
    def get(self,request,bank_account_id):
        bank_account = BankAccount.objects.get(bank_account_id=bank_account_id)
        self.add_to_context(bank_account=bank_account)
        return render(request, self.template, self.context)
    