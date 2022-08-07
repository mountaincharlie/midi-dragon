from django.shortcuts import render, redirect, reverse
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
