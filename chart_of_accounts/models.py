from django.db import models
from base.models import PyrlClient
from customers.models import Customer

sick_of_retyping = {
    'blank': False,
    'null': False
}

CLIENT_FK = models.ForeignKey(to=PyrlClient, on_delete=models.CASCADE)
CUSTOMER_FK = models.ForeignKey(to=Customer, on_delete=models.CASCADE, **sick_of_retyping)

class TransactionType(models.Model):
    class Meta:
        db_table = 'transaction_type'
        
    transaction_type = models.TextField(max_length=2, null=False)
    full_type_name = models.TextField(max_length=10, null=False)
    
    def __str__(self):
        return f'{self.transaction_type} - {self.full_type_name}'
    
class AccountType(models.Model):
    class Meta:
        db_table = 'account_type'
        
    account_type_id = models.BigAutoField(primary_key=True)
    description = models.TextField(max_length=50, null=False, blank=False)
    customer = CUSTOMER_FK
    expected_transaction_type = models.ForeignKey(to=TransactionType, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.description
    
class FinancialStatement(models.Model):
    class Meta:
        db_table = 'financial_statement'
        
    financial_statement_id = models.BigAutoField(primary_key=True)
    description = models.TextField(max_length=50, null=False, blank=False)
    customer = CUSTOMER_FK
    
    def __str__(self):
        return self.description

class Account(models.Model):
    class Meta:
        db_table = 'coa_account'
        
    account_id = models.BigAutoField(primary_key=True)
    nominal_code = models.TextField(max_length=15, **sick_of_retyping)
    description = models.TextField(max_length=30, **sick_of_retyping)
    account_type = models.ForeignKey(to=AccountType, on_delete=models.CASCADE, **sick_of_retyping)
    financial_statement = models.ForeignKey(to=FinancialStatement, on_delete=models.CASCADE, **sick_of_retyping)
    customer = CUSTOMER_FK
    
    def __str__(self):
        return f'{self.nominal_code} - {self.description}'
    
class ChartOfAccounts(models.Model):
    class Meta:
        db_table = 'chart_of_accounts'
        
    coa_id = models.BigAutoField(primary_key=True)
    description = models.TextField(**sick_of_retyping)
    customer = CUSTOMER_FK
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        string = f'{self.description}'
        if self.start_date:
            string = f'{string}, {self.start_date}'
            if self.end_date:
                string = f'{string} - {self.end_date}'
        return string
    
class CoaAccountLink(models.Model):
    class Meta:
        db_table = 'coa_account_link'
        
    coa = models.ForeignKey(to=ChartOfAccounts, on_delete=models.CASCADE, **sick_of_retyping)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, **sick_of_retyping)
    
    def __str__(self):
        return f'{self.coa.coa_id} - {self.account.account_type}'
    