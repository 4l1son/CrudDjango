from django.shortcuts import render
from .models import Vendedor

def lista_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/lista_vendedores.html', {'vendedores': vendedores})
