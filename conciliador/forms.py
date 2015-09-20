from django import forms

class Vendas(forms.Form):
    cliente_id = forms.CharField(
        label='Codigo do cliente', max_length=100)