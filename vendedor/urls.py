from django.urls import path
from .views import lista_vendedores

urlpatterns = [
    path('vendedor/', lista_vendedores, name='lista_vendedores'),
]
