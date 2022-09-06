""" test file for conducting tests on my tracklist.urls """

from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestTracklistUrls(TestCase):
    """
    TestTracklistUrls class inherits from Django's TestCase
    Contains all my tests on my tracklist.urls
    """

    def test_tracklist_url_resolves(self):
        """ tests if the songs url resolves """

        url = reverse('tracklist')
        self.assertEquals(resolve(url).func, views.view_tracklist)

    def test_add_to_tracklist_url_resolves(self):
        """ tests if the add_to_tracklist url resolves """

        url = reverse('add_to_tracklist', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.AddToTracklist)

    def test_remove_from_tracklist_url_resolves(self):
        """ tests if the remove_from_tracklist url resolves """

        url = reverse('remove_from_tracklist', args=['some-slug'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.RemoveFromTracklist
        )
