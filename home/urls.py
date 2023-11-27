from django.urls import path
from .views import home

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    # Adicione outras URLs conforme necessário
]
