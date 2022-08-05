from django.shortcuts import render
from django.views import generic, View
from .models import Song


class SongsList(generic.ListView):
    """
    Class based view inheriting Django's generic.ListView
    Uses the Song model for sending the searched for public songs to the
    songs.html template.
    """

    def get(self, request, *args, **kwargs):
        """
        Gets all of the songs which are public
        """
        public_songs = Song.objects.filter(public=True)

        context = {
            'songs': public_songs,
        }

        return render(request, "songs/songs.html", context)
