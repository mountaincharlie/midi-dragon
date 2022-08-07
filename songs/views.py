from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Song, Genre


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
        # regular users (logged in or not, can only view public songs)
        else:
            songs = Song.objects.filter(public=True)

        # resetting all vars
        query = None
        sort = None
        direction = None

        # ----------- credit- CI walkthrough for how to implement this
        # checking if sorting has been applied first
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            # using 'annotation' to add temporary field to model
            if sort_key == 'name':
                sort_key = 'lower_name'
                songs = songs.annotate(lower_name=Lower('name'))
            if sort_key == 'genre':
                # setting the songs to order by genre name if genre is the sorting criteria
                sort_key = 'genre__name'
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

        context = {
            'songs': songs,
            'song_search': query,
            'sort_parameters': selected_sorting,
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
