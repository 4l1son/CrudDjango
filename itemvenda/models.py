from django.db import models

# Create your models here.
class ItemVenda(models.Model):
    venda = models.CharField(max_length=255, unique=True)
    produto = models.CharField(max_length=255, unique=True)
    quantidade = models.CharField(max_length=255, unique=True)
    preco_unitario = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.venda
