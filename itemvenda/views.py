from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemVenda
from .forms import ItemVendaForm

def lista_itemvenda(request):
    itemvendas = ItemVenda.objects.all()
    return render(request, 'itemvenda/lista_itemvenda.html', {'itemvendas': itemvendas})

def detalhes_itemvenda(request, itemvenda_id):
    itemvenda = get_object_or_404(ItemVenda, pk=itemvenda_id)
    return render(request, 'itemvenda/detalhes_itemvenda.html', {'itemvenda': itemvenda})

def adicionar_itemvenda(request):
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itemvenda:lista_itemvenda')
    else:
        form = ItemVendaForm()
    return render(request, 'itemvenda/adicionar_itemvenda.html', {'form': form})

def editar_itemvenda(request, itemvenda_id):
    itemvenda = get_object_or_404(ItemVenda, pk=itemvenda_id)
    if request.method == 'POST':
        form = ItemVendaForm(request.POST, instance=itemvenda)
        if form.is_valid():
            form.save()
            return redirect('itemvenda:lista_itemvenda')
    else:
        form = ItemVendaForm(instance=itemvenda)
    return render(request, 'itemvenda/editar_itemvenda.html', {'form': form, 'itemvenda': itemvenda})

def excluir_itemvenda(request, itemvenda_id):
    itemvenda = get_object_or_404(ItemVenda, pk=itemvenda_id)
    if request.method == 'POST':
        itemvenda.delete()
        return redirect('itemvenda:lista_itemvenda')
    return render(request, 'itemvenda/excluir_itemvenda.html', {'itemvenda': itemvenda})
