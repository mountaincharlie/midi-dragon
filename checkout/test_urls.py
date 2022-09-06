""" test file for conducting tests on my checkout.urls """

from django.test import TestCase
from django.urls import reverse, resolve
from . import views
from .webhooks import webhook


class TestCheckoutUrls(TestCase):
    """
    TestCheckoutUrls class inherits from Django's TestCase
    Contains all my tests on my checkout.urls
    """

    def test_checkout_url_resolves(self):
        """ tests if the checkout url resolves """

        url = reverse('checkout')
        self.assertEquals(resolve(url).func.view_class, views.CheckoutView)

    def test_order_confirmation_url_resolves(self):
        """ tests if the order_confirmation url resolves """

        url = reverse('order_confirmation', args=['123456'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.OrderConfirmation
        )

    def test_cache_checkout_data_url_resolves(self):
        """ tests if the cache_checkout_data url resolves """

        url = reverse('cache_checkout_data')
        self.assertEquals(
            resolve(url).func,
            views.cache_checkout_data
        )

    def test_webhook_url_resolves(self):
        """ tests if the webhook url resolves """

        url = reverse('webhook')
        self.assertEquals(
            resolve(url).func,
            webhook
        )
