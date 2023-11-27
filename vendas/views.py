from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendas
from .forms import VendasForm

def lista_vendas(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas/lista_vendas.html', {'vendas': vendas})

def detalhes_venda(request, venda_id):
    venda = get_object_or_404(Vendas, pk=venda_id)
    return render(request, 'vendas/detalhes_vendas.html', {'venda': venda})

def adicionar_venda(request):
    if request.method == 'POST':
        form = VendasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendas:lista_vendas')
    else:
        form = VendasForm()
    return render(request, 'vendas/adicionar_vendas.html', {'form': form})

def editar_venda(request, venda_id):
    venda = get_object_or_404(Vendas, pk=venda_id)
    if request.method == 'POST':
        form = VendasForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('vendas:lista_vendas')
    else:
        form = VendasForm(instance=venda)
    return render(request, 'vendas/editar_vendas.html', {'form': form, 'venda': venda})

def excluir_venda(request, venda_id):
    venda = get_object_or_404(Vendas, pk=venda_id)
    if request.method == 'POST':
        venda.delete()
        return redirect('vendas:lista_vendas')
    return render(request, 'vendas/excluir_vendas.html', {'venda': venda})
