from django import forms
from .models import Customer, CustomerContact
from ui.widget_library import TestCustomWidget, EmailWidget, TestTextWidget
from django.forms import model_to_dict

class CustomerForm(forms.ModelForm):
    label_suffix = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Customer
        fields = ['display_name','legal_entity']
        widgets = {
            'display_name': TestCustomWidget(attrs={'placeholder':'Hi', 'label': 'Display Name'})
        }
        
        labels ={
            'display_name': '',
            'legal_entity': ''
        }
        
class CustomerContactForm(forms.ModelForm):
    label_suffix = None
    
    class Meta:
        model = CustomerContact
        fields = [
            'forename', 
            'surname', 
            'date_of_birth', 
            'email_address'
        ]
        widgets = {
            'forename': TestTextWidget(attrs={'placeholder': 'Forename', 'label':'Forename'}),
            'surname': TestTextWidget(attrs={'placeholder': 'Surname', 'label':'Surname'}),
            'date_of_birth': TestTextWidget(attrs={'placeholder': 'Surname', 'label':'Date of Birth'}),
            'email_address': TestTextWidget(attrs={'placeholder': 'Surname', 'label':'Email Address'})
        }
        labels = {
            'forename': '',
            'surname': '',
            'date_of_birth': '',
            'email_address': ''
        }
    
    def __init__(self, prefill_data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if prefill_data is not None:
            data = model_to_dict(prefill_data)
            for key, val in data.items():
                if key in self.fields:
                    self.fields[key].initial = val
                    print('found')
                
        
        