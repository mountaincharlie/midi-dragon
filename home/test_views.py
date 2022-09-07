""" test file for conducting tests on my home.views """

from django.test import TestCase, Client
from django.urls import reverse


class TestHomeViews(TestCase):
    """
    TestHomeViews class inherits from Django's TestCase
    Contains all my tests on my home.views
    """

    def test_index_get(self):
        """ tests if the index function view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_faqs_get(self):
        """ tests if the faqs function view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/FAQs.html')

    def test_tos_get(self):
        """ tests if the tos function view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('tos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/terms_of_service.html')

    def test_privacy_get(self):
        """ tests if the privacy function view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('privacy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy_policy.html')
