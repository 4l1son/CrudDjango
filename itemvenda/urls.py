from django.urls import path
from .views import lista_itemvenda, adicionar_itemvenda, detalhes_itemvenda, editar_itemvenda, excluir_itemvenda

app_name = 'itemvenda'

urlpatterns = [
    path('itemvenda/', lista_itemvenda, name='lista_itemvenda'),
    path('itemvenda/adicionar/', adicionar_itemvenda, name='adicionar_itemvenda'),
    path('itemvenda/<int:itemvenda_id>/', detalhes_itemvenda, name='detalhes_itemvenda'),
    path('itemvenda/<int:itemvenda_id>/editar/', editar_itemvenda, name='editar_itemvenda'),
    path('itemvenda/<int:itemvenda_id>/excluir/', excluir_itemvenda, name='excluir_itemvenda'),
]
