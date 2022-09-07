""" apps.py for the checkout app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ overrides the ready method """
        import checkout.signals
