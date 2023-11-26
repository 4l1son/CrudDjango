from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome
