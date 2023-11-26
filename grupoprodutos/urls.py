from django.urls import path
from .views import lista_grupoprodutos

urlpatterns = [
    path('grupoprodutos/', lista_grupoprodutos, name='lista_grupoprodutos'),
]
