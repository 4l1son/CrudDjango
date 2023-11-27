from django import forms
from .models import GrupoProduto

class GrupoProdutoForm(forms.ModelForm):
    class Meta:
        model = GrupoProduto
        fields = ['nome', 'descricao']
