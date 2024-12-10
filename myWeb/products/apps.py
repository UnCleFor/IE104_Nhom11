from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

# trong apps.py của app 'products'
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        # không cần gọi import từ signals.py
        pass
