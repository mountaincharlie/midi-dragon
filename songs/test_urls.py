""" test file for conducting tests on my songs.urls """

from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestSongsUrls(TestCase):
    """
    TestSongsUrls class inherits from Django's TestCase
    Contains all my tests on my songs.urls
    """

    def test_songs_url_resolves(self):
        """ tests if the songs url resolves """

        url = reverse('songs')
        self.assertEquals(resolve(url).func.view_class, views.SongsList)

    def test_testimonials_url_resolves(self):
        """ tests if the testimonials url resolves """

        url = reverse('testimonials')
        self.assertEquals(resolve(url).func.view_class, views.TestimonialsList)

    def test_design_custom_song_url_resolves(self):
        """ tests if the design_custom_song url resolves """

        url = reverse('design_custom_song')
        self.assertEquals(resolve(url).func.view_class, views.DesignCustomSong)

    def test_edit_custom_song_url_resolves(self):
        """ tests if the edit_custom_song url resolves """

        url = reverse('edit_custom_song', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.EditCustomSong)

    def test_delete_confirmation_url_resolves(self):
        """ tests if the delete_confirmation url resolves """

        url = reverse('delete_confirmation', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.DeleteSong)

    def test_song_details_url_resolves(self):
        """ tests if the song_details url resolves """

        url = reverse('song_details', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.SongDetailsView)

    def test_song_like_url_resolves(self):
        """ tests if the song_like url resolves """

        url = reverse('song_like', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.LikeSong)
