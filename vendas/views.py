
# produtos/views.py
from django.shortcuts import render
from .models import Vendas

def lista_vendas(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas/lista_vendas.html', {'vendas': vendas})
 