
# produtos/views.py
from django.shortcuts import render
from .models import ItemVenda

def lista_itemvenda(request):
    itemvenda = ItemVenda.objects.all()
    return render(request, 'itemvenda/lista_itemvenda.html', {'itemvenda': itemvenda})
 