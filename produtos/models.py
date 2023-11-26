from django.db import models

class Produto(models.Model):
    nomeProduto = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nomeProduto
