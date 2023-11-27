from django.urls import path
from .views import lista_grupoprodutos, adicionar_grupoproduto, detalhes_grupoproduto, editar_grupoproduto, excluir_grupoproduto

app_name = 'grupoprodutos'

urlpatterns = [
    path('/', lista_grupoprodutos, name='lista_grupoprodutos'),
    path('grupoprodutos/adicionar/', adicionar_grupoproduto, name='adicionar_grupoproduto'),
    path('grupoprodutos/<int:grupoproduto_id>/', detalhes_grupoproduto, name='detalhes_grupoproduto'),
    path('grupoprodutos/<int:grupoproduto_id>/editar/', editar_grupoproduto, name='editar_grupoproduto'),
    path('grupoprodutos/<int:grupoproduto_id>/excluir/', excluir_grupoproduto, name='excluir_grupoproduto'),
]
