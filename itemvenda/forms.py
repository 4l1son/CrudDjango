from django import forms
from .models import ItemVenda

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['venda', 'produto', 'quantidade', 'preco_unitario']
