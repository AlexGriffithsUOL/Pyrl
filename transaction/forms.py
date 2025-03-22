from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'reference_description',
            'account',
            'net',
            'vat_type',
            'vat',
            'gross',
            'date_of_transaction'
        ]