# clientes/urls.py
from django.urls import path
from .views import lista_clientes, adicionar_cliente, detalhes_cliente, editar_cliente, excluir_cliente

app_name = 'clientes'

urlpatterns = [
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('adicionar/', adicionar_cliente, name='adicionar_cliente'),
    path('<int:cliente_id>/', detalhes_cliente, name='detalhes_cliente'),
    path('<int:cliente_id>/editar/', editar_cliente, name='editar_cliente'),
    path('<int:cliente_id>/excluir/', excluir_cliente, name='excluir_cliente'),
]
