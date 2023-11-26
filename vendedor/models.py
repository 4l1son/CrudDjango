# Example model in vendedor/models.py
from django.db import models

class Vendedor(models.Model):
    # Your fields and definitions here
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    # ... other fields ...

    def __str__(self):
        return self.nome
