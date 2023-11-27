from django.urls import path
from .views import lista_vendedores, adicionar_vendedor, detalhes_vendedor, editar_vendedor, excluir_vendedor

app_name = 'vendedor'

urlpatterns = [
    path('', lista_vendedores, name='lista_vendedores'),
    path('vendedores/adicionar/', adicionar_vendedor, name='adicionar_vendedor'),
    path('vendedores/<int:vendedor_id>/', detalhes_vendedor, name='detalhes_vendedor'),
    path('vendedores/<int:vendedor_id>/editar/', editar_vendedor, name='editar_vendedor'),
    path('vendedores/<int:vendedor_id>/excluir/', excluir_vendedor, name='excluir_vendedor'),
]
