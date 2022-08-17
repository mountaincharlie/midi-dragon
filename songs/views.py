from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Song, Genre
from django.contrib.auth.models import User
from django.http import HttpResponse
import mimetypes


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
        # only the admin can view all of the songs
        if request.user.is_superuser:
            songs = Song.objects.all()
        # for regular users (logged in or not, can only browse public pre-made songs)
        else:
            # pre-made songs are those where the admin is the user
            superuser_name = User.objects.get(is_superuser=True)
            premade_songs = Song.objects.filter(user=superuser_name)
            # filtering these songs by only public ones
            songs = premade_songs.filter(public=True)

        # getting all of the genres
        genres = Genre.objects.all()

        # resetting all vars
        query = None
        sort = None
        direction = None
        selected_genre = None
        selected_genre_display_name = None

        # ----------- credit- CI walkthrough for how to implement this
        # checking if sorting has been applied first
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            # using 'annotation' to add temporary field to model
            if sort_key == 'name':
                sort_key = 'lower_name'
                songs = songs.annotate(lower_name=Lower('name'))
            # if sort_key == 'genre':
            #     # setting the songs to order by genre name if genre is the sorting criteria
            #     sort_key = 'genre__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                # check if its decending so you add a '-' before
                if direction == 'desc':
                    sort_key = f'-{sort_key}'

            # ordering the songs
            songs = songs.order_by(sort_key)

        # if query (name attribute on search form input) exists, we need to get its value
        if 'query' in request.GET:
            query = request.GET['query']
            # handling blank search with django message and redirect
            if not query:
                # include error message with django messages
                # reverse here just reloads the page
                return redirect(reverse('songs'))

            # using Django's Q to check if the search is in name OR any details
            queries = (
                Q(name__icontains=query)
                | Q(song_purpose__icontains=query)
                | Q(song_feel__icontains=query)
                | Q(additional_details__icontains=query)
            )

            songs = songs.filter(queries)

        # defining the current sorting
        selected_sorting = f'{sort}_{direction}'

        # checking if the genre filter has been applied
        if 'genre' in request.GET:
            selected_genre = request.GET['genre']
            # print('select value?', selected_genre)
            genre = Genre.objects.get(name=selected_genre)
            selected_genre_display_name = genre.display_name
            # print('selected genre:', genre.pk)
            songs = songs.filter(genre=genre.pk)

        context = {
            'songs': songs,
            'song_search': query,
            'sort_parameters': selected_sorting,
            'genres': genres,
            'selected_genre': selected_genre,
            'selected_genre_display_name': selected_genre_display_name,
        }

        return render(request, "songs/songs.html", context)


class SongDetailsView(View):
    """
    Class based view inheriting Django's View
    Contains the get method for displaying the details for a chosen
    song by its slug.
    """
    def get(self, request, *args, **kwargs):
        """
        get method for when users click on a song's image or name to
        see the song's full details.
        -gets all of the Song objects
        -gets the chosen song by its slug
        -sets a like variable as False
        -checks if the current user has given a like to this song
        -if so, it sets like as True(so that the like icon will be highlighted
        in the song_details template)
        -sets context dict with the song and its like status
        -renders song_details.html with the request and context data
        """
        songs = Song.objects.all()
        song = get_object_or_404(songs, slug=self.kwargs['slug'])

        # setting like as False until its confirmed it has likes
        like = False
        if song.likes.filter(id=self.request.user.id).exists():
            like = True

        context = {
            'song': song,
            'like': like,
        }

        return render(request, 'songs/song_details.html', context)


class DownloadSong(View):
    """
    Class based view inheriting Django's View
    Contains the get method for downloading the audio_file
    for a particular song
    """
    def get(self, request, *args, **kwargs):
        """
        Gets the song by its slug.
        Creates the filename which is the string of its audio_file name.
        Sets the file path which is the filename in the media folder.
        Opens the file for reading in binary (rb).
        Uses mimetypes to guess the mime type for the file (will be .mp3 or .wav)
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        filename = str(song.audio_file)
        file_path = 'media/'+filename
        mime_type = filename.split('.')[1]

        # logic for opening the file and allowing it to be downloaded from adapted from (CREDIT - https://djangoadventures.com/how-to-create-file-download-links-in-django/)
        read_file = open(file_path, 'rb')
        # print('mimetype:', mime_type)
        response = HttpResponse(read_file, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response
