""" test file for conducting tests on my home.urls """

from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestHomeUrls(TestCase):
    """
    TestHomeUrls class inherits from Django's TestCase
    Contains all my tests on my home.urls
    """

    def test_home_url_resolves(self):
        """ tests if the home url resolves """

        url = reverse('home')
        self.assertEquals(resolve(url).func, views.index)

    def test_faqs_url_resolves(self):
        """ tests if the faqs url resolves """

        url = reverse('faqs')
        self.assertEquals(resolve(url).func, views.faqs)

    def test_tos_url_resolves(self):
        """ tests if the tos url resolves """

        url = reverse('tos')
        self.assertEquals(resolve(url).func, views.tos)

    def test_privacy_url_resolves(self):
        """ tests if the privacy url resolves """

        url = reverse('privacy')
        self.assertEquals(resolve(url).func, views.privacy)
