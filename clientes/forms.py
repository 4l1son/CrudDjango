# No seu arquivo forms.py dentro do aplicativo 'clientes'

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']
