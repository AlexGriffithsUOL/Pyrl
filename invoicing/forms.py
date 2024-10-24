from django import forms
from products.models import product
from custom_widgets.widgets import SelectInput, CustomTextInput, DecimalInput, CurrencyInput, InvoiceTextInput

class row_form(forms.Form):
    country = forms.ModelChoiceField(
            queryset= product.objects.all(),
            to_field_name='name',
            required=True,
            widget=SelectInput
        )
    description = forms.DecimalField(
        widget=InvoiceTextInput,
        max_digits=10,
        decimal_places=2
    )
    quantity = forms.DecimalField(
        widget=DecimalInput,
        max_digits=10,
        decimal_places=2
    )
    rate = forms.DecimalField(
        widget=CurrencyInput,
        max_digits=10,
        decimal_places=2
    )
    
    class Meta:
        fields = ['country']
        field_names = ['country']