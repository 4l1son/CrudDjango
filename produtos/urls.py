from django.urls import path
from .views import lista_produtos, adicionar_produto, detalhes_produto, editar_produto, excluir_produto

app_name = 'produtos'

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', adicionar_produto, name='adicionar_produto'),
    path('produtos/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('produtos/<int:produto_id>/editar/', editar_produto, name='editar_produto'),
    path('produtos/<int:produto_id>/excluir/', excluir_produto, name='excluir_produto'),
]
