from django.apps import AppConfig

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

    def ready(self):
        try:
            import produtos.signals  # Import signals here if you have any
        except ImportError:
            pass
