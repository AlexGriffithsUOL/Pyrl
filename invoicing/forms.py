from django import forms
from products.models import product
from ui.widget_library import TestCustomWidget

class row_form(forms.Form):
    country = forms.ModelChoiceField(
            queryset= product.objects.all(),
            to_field_name='name',
            required=True,
            widget=TestCustomWidget()
        )
    description = forms.DecimalField(
        widget=TestCustomWidget(),
        max_digits=10,
        decimal_places=2
    )
    quantity = forms.DecimalField(
        widget=TestCustomWidget(),
        max_digits=10,
        decimal_places=2
    )
    rate = forms.DecimalField(
        widget=TestCustomWidget(),
        max_digits=10,
        decimal_places=2
    )
    
    class Meta:
        fields = ['country']
        field_names = ['country']