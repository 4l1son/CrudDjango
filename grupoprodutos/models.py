# grupoprodutos/models.py

from django.db import models

class GrupoProduto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
