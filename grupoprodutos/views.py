from django.shortcuts import render, get_object_or_404, redirect
from .models import GrupoProduto
from .forms import GrupoProdutoForm

def lista_grupoprodutos(request):
    grupoprodutos = GrupoProduto.objects.all()
    return render(request, 'grupoprodutos/lista_grupoprodutos.html', {'grupoprodutos': grupoprodutos})

def detalhes_grupoproduto(request, grupoproduto_id):
    grupoproduto = get_object_or_404(GrupoProduto, pk=grupoproduto_id)
    return render(request, 'grupoprodutos/detalhes_grupoproduto.html', {'grupoproduto': grupoproduto})

def adicionar_grupoproduto(request):
    if request.method == 'POST':
        form = GrupoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupoprodutos:lista_grupoprodutos')
    else:
        form = GrupoProdutoForm()
    return render(request, 'grupoprodutos/adicionar_grupoproduto.html', {'form': form})

def editar_grupoproduto(request, grupoproduto_id):
    grupoproduto = get_object_or_404(GrupoProduto, pk=grupoproduto_id)
    if request.method == 'POST':
        form = GrupoProdutoForm(request.POST, instance=grupoproduto)
        if form.is_valid():
            form.save()
            return redirect('grupoprodutos:lista_grupoprodutos')
    else:
        form = GrupoProdutoForm(instance=grupoproduto)
    return render(request, 'grupoprodutos/editar_grupoproduto.html', {'form': form, 'grupoproduto': grupoproduto})

def excluir_grupoproduto(request, grupoproduto_id):
    grupoproduto = get_object_or_404(GrupoProduto, pk=grupoproduto_id)
    if request.method == 'POST':
        grupoproduto.delete()
        return redirect('grupoprodutos:lista_grupoprodutos')
    return render(request, 'grupoprodutos/excluir_grupoproduto.html', {'grupoproduto': grupoproduto})
