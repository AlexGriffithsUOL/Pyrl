from django.shortcuts import render
from base.views import PageView
from django.http import JsonResponse
from .forms import TransactionForm
from .models import Transaction
from banking.begin import get_plaid_client
from banking.models import BankAccount
from customers.models import Customer
from chart_of_accounts.models import TransactionType, Account, CoaAccountLink, ChartOfAccounts
from plaid.models import TransactionsSyncRequest, TransactionsSyncResponse

def inner_join(object_1, object_2, customer_id):
    print(object_1)
    print(object_2)
    query = f'''select t.transaction_id
            from transaction t 
            inner join coa_account_link coal on coal.account_id = t.account_id
            inner join chart_of_accounts coa on coa.coa_id = coal.coa_id
            where coa.customer_id = {customer_id};'''
    return Transaction.objects.raw(query)

# Create your views here.
class TransactionCreateView(PageView):
    template = 'main_app/transaction/create.html'
    page_title = 'Create a transaction'
    
    def get(self, request, customer_id):
        super().__init__(request=request,page_title=self.page_title)
        debit_transaction_type = TransactionType.objects.get(transaction_type='Dr')
        credit_transaction_type = TransactionType.objects.get(transaction_type='Cr')
        dr_tr_form = TransactionForm({'transaction_type':debit_transaction_type})
        cr_tr_form = TransactionForm({'transaction_type': credit_transaction_type})
        self.add_to_context(dr_tr_form=dr_tr_form)
        self.add_to_context(cr_tr_form=cr_tr_form)
        return render(request, self.template, self.context)
    
    def post(self, request, customer_id):
        post_data = request.POST.dict()
        print(post_data)
        del post_data['csrfmiddlewaretoken']
        f1 = TransactionForm(request.POST)
        f2 = TransactionForm(request.POST)
        post_data['transaction_type'] = TransactionType.objects.get(id=post_data['transaction_type'])
        post_data['account'] = Account.objects.get(account_id=post_data['account'])
        new_transaction = Transaction(**post_data)
        new_transaction.net = float(new_transaction.net)
        
        vat = 0.0
        if not post_data['vat'] or post_data['vat'] == '':
            new_transaction.vat = new_transaction.calculate_vat()
            print(new_transaction.vat)
                # Subquery to find the contact's phone number for each client
        gross = 0.0
        if not post_data['gross'] or post_data['gross'] == '':
            new_transaction.gross = new_transaction.calculate_gross()    
            
        new_transaction.save()
        
        return render(request, template_name='404.html', context=self.context)
    
class GeneralLedgerView(PageView):
    
    template = 'main_app/chart_of_accounts/general_ledger.html'
    page_title = 'General Ledger'
    
    def get(self, request, customer_id):
        from django.db.models import OuterRef, Subquery

        # contact_subquery = Contact.objects.filter(client_email=OuterRef('email')).values('phone_number')[:1]

        # clients = Client.objects.annotate(phone_number=Subquery(contact_subquery))
        from django import urls

        url_resolver = urls.get_resolver(urls.get_urlconf())
        
        print(url_resolver.namespace_dict.keys())
        super().__init__(template=self.template,page_title=self.page_title)
        transactions = inner_join(Transaction, CoaAccountLink, customer_id=customer_id)
        
        # transactions = Transaction.objects.select_related('coa_account_link').filter()
        print(transactions)
        self.add_to_context(transactions=transactions)
        self.add_to_context(customer_id=customer_id)
        return render(request, self.template, self.context)
        
class RefreshTransactions(PageView):
    template = 'main_app/transaction/refresh.html'
    page_title = 'TEST'
    
    def get(self, request):
        plaid_client = get_plaid_client()
        access_token = Customer.objects.get(customer_id=1).plaid_access_token
        plaid_request = TransactionsSyncRequest(
            access_token=access_token
        )

        plaid_response:TransactionsSyncResponse = plaid_client.transactions_sync(plaid_request) ###YOU NEED TO COME HERE AND GO THROUGH TRANSACTIONS
        # DATABASE DESIGN NEEDED, INTERMEDIARY TRANSACTION STAGE???
        plaid_response2 = plaid_response.to_dict()
        
        for account in plaid_response2['accounts']:  
            try:
                acc = BankAccount.objects.get(bank_account_id=account['account_id'])
            except Exception as e:
                print('failed')
        
        ### Try to find account
        
        
        
        ### if account can be found then update transactions
        
        ### else create new account and add transactions
        
        
        print(plaid_response.accounts)
        print(plaid_response._data_store)
            
        return JsonResponse({'data':plaid_response})