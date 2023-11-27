from django.urls import path
from .views import lista_vendas, adicionar_venda, detalhes_venda, editar_venda, excluir_venda

app_name = 'vendas'

urlpatterns = [
    path('vendas/', lista_vendas, name='lista_vendas'),
    path('vendas/adicionar/', adicionar_venda, name='adicionar_venda'),
    path('vendas/<int:venda_id>/', detalhes_venda, name='detalhes_venda'),
    path('vendas/<int:venda_id>/editar/', editar_venda, name='editar_venda'),
    path('vendas/<int:venda_id>/excluir/', excluir_venda, name='excluir_venda'),
]
