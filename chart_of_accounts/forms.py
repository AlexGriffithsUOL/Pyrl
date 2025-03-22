from django import forms
from .models import ChartOfAccounts, AccountType, FinancialStatement, Account, CoaAccountLink

class ChartOfAccountsForm(forms.ModelForm):
    class Meta:
        model = ChartOfAccounts
        fields = [
            'description',
            'start_date',
            'end_date'
        ]
        
class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = [
            'description',
            'expected_transaction_type'
        ]
        
class FinancialStatementForm(forms.ModelForm):
    class Meta:
        model = FinancialStatement
        fields = [
            'description'
        ]
        
class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = [
            'nominal_code',
            'description',
            'account_type',
            'financial_statement'    
        ]

class CoaAccountLinkForm(forms.ModelForm):
    class Meta:
        model=CoaAccountLink
        fields = [
            'coa',
            'account'
        ]