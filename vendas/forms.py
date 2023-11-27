from django import forms
from .models import Vendas

class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome_cliente', 'valor_total']
