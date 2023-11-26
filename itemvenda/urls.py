from django.urls import path
from .views import lista_itemvenda

urlpatterns = [
    path('itemvenda/', lista_itemvenda, name='lista_itemvenda'),
]
