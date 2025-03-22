from django.shortcuts import render, redirect
from base.views import PageView
from .models import ChartOfAccounts, Account, AccountType, FinancialStatement, CoaAccountLink, TransactionType
from customers.models import Customer
from .forms import ChartOfAccountsForm, AccountTypeForm, FinancialStatementForm, AccountForm, CoaAccountLinkForm
from transaction.models import Transaction

COA_TEMPLATE_PREFIX = 'main_app/chart_of_accounts'

class ChartOfAccountsViews:
    class ChartOfAccountsListView(PageView):
        template = 'main_app/chart_of_accounts/list.html'
        page_title = 'Chart of Accounts'

        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            customer = Customer.objects.get(customer_id=customer_id)
            chart_of_accounts = ChartOfAccounts.objects.filter(customer=customer)
            
            real_coa = []
            temp_link = ''
            for coa in chart_of_accounts:
                obj = {
                    'description': coa.description,
                    'start_date': coa.start_date,
                    'end_date': coa.end_date,
                    'links': CoaAccountLink.objects.filter(coa_id=coa.coa_id)
                }
                temp_link = CoaAccountLink.objects.filter(coa_id=coa.coa_id)[0]
                real_coa.append(obj)
            
            self.add_to_context(real_coa=real_coa)
            self.add_to_context(customer_id=customer_id)
            return render(request, self.template, self.context)
        
    class ChartOfAccountsCreateView(PageView):
        template = 'main_app/chart_of_accounts/create_edit.html'
        page_title = 'Create a Chart of Accounts'
        
        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            coa_form = ChartOfAccountsForm
            self.add_to_context(coa_form=coa_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id):
            post_data = request.POST.dict()
            
            del post_data['csrfmiddlewaretoken']
            
            if post_data['start_date'] == '':
                del post_data['start_date']
                
            if post_data['end_date'] == '':
                del post_data['end_date']
            
            post_data['customer'] = Customer.objects.get(customer_id=customer_id)
            
            ChartOfAccounts(
                    **post_data
            ).save()
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
        
    class ChartOfAccountsEditView(PageView):
        template = 'main_app/chart_of_accounts/create_edit.html'
        page_title = 'Edit a Chart of Accounts'
        
        def get(self, request, coa_id, *args, **kwargs):
            coa_form = ChartOfAccountsForm(instance=ChartOfAccounts.objects.get(coa_id=coa_id))
            self.add_to_context(coa_form=coa_form)
            self.add_to_context(edit=True)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id, coa_id):
            post_data = request.POST.dict()
            
            del post_data['csrfmiddlewaretoken']
            
            chart_of_accounts = ChartOfAccounts.objects.get(coa_id=coa_id)
            chart_of_accounts.description = post_data['description']
            
            if post_data['start_date'] != '':
                chart_of_accounts.start_date = post_data['start_date']
                
            if post_data['end_date'] != '':
                chart_of_accounts.end_date = post_data['end_date']
            
            chart_of_accounts.save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
    
class AccountTypeViews:
    class AccountTypeCreateView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/account_type/create.html'
        page_title = 'Create an Account Type'
        
        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            at_form = AccountTypeForm
            self.add_to_context(at_form=at_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id):
            post_data = request.POST.dict()        
            del post_data['csrfmiddlewaretoken']
            
            post_data['expected_transaction_type'] = TransactionType.objects.get(id=post_data['expected_transaction_type'])
            post_data['customer'] = Customer.objects.get(customer_id=customer_id)
            
            AccountType(
                **post_data
            ).save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
        
    class AccountTypeEditView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/account_type/create.html'
        page_title = 'Edit an Account Type'
        
        def get(self, request, at_id, *args, **kwargs):
            at_form = AccountTypeForm(instance=AccountType.objects.get(account_type_id=at_id))
            self.add_to_context(at_form=at_form)
            return render(self.request, self.template, self.context)
        
        def post(self, request, customer_id, at_id):
            post_data = request.POST.dict()
            del post_data['csrfmiddlewaretoken']
            
            account_type = AccountType.objects.get(account_type_id=at_id)
            account_type.description = post_data['description']
            account_type.expected_transaction_type = TransactionType.objects.get(id=post_data['expected_transaction_type'])
            
            account_type.save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
        
class FinancialStatementViews:
    class FinancialStatementCreateView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/financial_statement/create.html'
        page_title = 'Create a Financial Statement'
        
        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            fs_form = FinancialStatementForm
            self.add_to_context(fs_form=fs_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id):
            post_data = request.POST.dict()        
            del post_data['csrfmiddlewaretoken']
            
            post_data['customer'] = Customer.objects.get(customer_id=customer_id)
            
            FinancialStatement(
                **post_data
            ).save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)    

    class FinancialStatementEditView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/financial_statement/create.html'
        page_title = 'Edit a Financial Statement'
        
        def get(self, request, fs_id, *args, **kwargs):
            super().__init__(request=request,page_title=self.page_title)
            fs_form = FinancialStatementForm(instance=FinancialStatement.objects.get(financial_statement_id=fs_id))
            self.add_to_context(fs_form=fs_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id, fs_id):
            post_data = request.POST.dict()        
            del post_data['csrfmiddlewaretoken']
            
            financial_statement = FinancialStatement.objects.get(financial_statement_id=fs_id)
            financial_statement.description = post_data['description']
            financial_statement.save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)    
  
class AccountViews:
    class AccountCreateView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/account/create.html'
        page_title = 'Create an account'
        
        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            acc_form = AccountForm
            self.add_to_context(acc_form=acc_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id):
            post_data = request.POST.dict()        
            
            del post_data['csrfmiddlewaretoken']
            
            post_data['account_type'] = AccountType.objects.get(account_type_id=post_data['account_type'])
            post_data['financial_statement'] = FinancialStatement.objects.get(financial_statement_id=post_data['financial_statement'])
            post_data['customer'] = Customer.objects.get(customer_id=customer_id)
            
            Account(
                **post_data
            ).save()
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
        
    class AccountEditView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/account/create.html'
        page_title = 'Edit an account'
        
        def get(self, request, acc_id, *args, **kwargs):
            super().__init__(request=request,page_title=self.page_title)
            acc_form = AccountForm(instance=Account.objects.get(account_id=acc_id))
            self.add_to_context(acc_form=acc_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id, acc_id):
            post_data = request.POST.dict()        
            
            del post_data['csrfmiddlewaretoken']
            
            account = Account.objects.get(account_id=acc_id)
            account.nominal_code = post_data['nominal_code']
            account.description = post_data['description']
            account.account_type = AccountType.objects.get(account_type_id=post_data['account_type'])
            account.financial_statement = FinancialStatement.objects.get(financial_statement_id=post_data['financial_statement'])
            account.save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
    
class CoaAccountLinkViews:
    
    class CoaAccountLinkCreateView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/coa_account_link/create.html'
        page_title = 'Create a COA Link'
        
        def get(self, request, customer_id):
            super().__init__(request=request,page_title=self.page_title)
            cal_form = CoaAccountLinkForm
            self.add_to_context(cal_form=cal_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id):
            post_data = request.POST.dict()        
            
            del post_data['csrfmiddlewaretoken']
            
            post_data['coa'] = ChartOfAccounts.objects.get(coa_id=post_data['coa'])
            post_data['account'] = Account.objects.get(account_id=post_data['account'])
            
            CoaAccountLink(
                **post_data
            ).save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)
        
    class CoaAccountLinkEditView(PageView):
        template = f'{COA_TEMPLATE_PREFIX}/coa_account_link/create.html'
        page_title = 'Edit a COA Link'
        
        def get(self, request, cal_id, *args, **kwargs):
            super().__init__(request=request,page_title=self.page_title)
            cal_form = CoaAccountLinkForm(instance=CoaAccountLink.objects.get(id=cal_id))
            self.add_to_context(cal_form=cal_form)
            return render(request, self.template, self.context)
        
        def post(self, request, customer_id, cal_id):
            post_data = request.POST.dict()        
            
            del post_data['csrfmiddlewaretoken']
            
            coa_account_link = CoaAccountLink.objects.get(id=cal_id)
            coa_account_link.coa = ChartOfAccounts.objects.get(coa_id=post_data['coa'])
            coa_account_link.account = Account.objects.get(account_id=post_data['account'])
            coa_account_link.save()
            
            return redirect('main_app:chart_of_accounts:coa_list', customer_id=customer_id)