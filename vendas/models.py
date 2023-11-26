# Example model in vendas/models.py
from django.db import models

class Vendas(models.Model):
    # Your fields and definitions here
    nome_cliente = models.CharField(max_length=100)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    # ... other fields ...

    def __str__(self):
        return self.nome_cliente
