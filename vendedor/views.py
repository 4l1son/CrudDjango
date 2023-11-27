from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendedor
from .forms import VendedorForm

def lista_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/lista_vendedores.html', {'vendedores': vendedores})

def detalhes_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    return render(request, 'vendedor/detalhes_vendedor.html', {'vendedor': vendedor})

def adicionar_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor:lista_vendedores')
    else:
        form = VendedorForm()
    return render(request, 'vendedor/adicionar_vendedor.html', {'form': form})

def editar_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor:lista_vendedores')
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, 'vendedor/editar_vendedor.html', {'form': form, 'vendedor': vendedor})

def excluir_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    if request.method == 'POST':
        vendedor.delete()
        return redirect('vendedor:lista_vendedores')
    return render(request, 'vendedor/excluir_vendedor.html', {'vendedor': vendedor})
