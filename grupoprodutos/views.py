
# produtos/views.py
from django.shortcuts import render
from .models import GrupoProduto

def lista_grupoprodutos(request):
    grupoprodutos = GrupoProduto.objects.all()
    return render(request, 'grupoprodutos/lista_grupoprodutos.html', {'grupoprodutos': grupoprodutos})
 