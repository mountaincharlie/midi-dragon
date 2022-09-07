""" views.py for the songs app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from django.db.models import Q
from django.db.models.functions import Lower
from django.conf import settings
from django.contrib.auth.models import User
from checkout.models import Order, OrderSong
from .models import Song, Genre, SongInstrument, Instrument, ProjectType
from .forms import DesignCustomSongForm, AddSongInstrumentFormSet


class SongsList(generic.ListView):
    """
    Class based view inheriting Django's generic.ListView
    Uses the Song model for sending the searched for public songs to the
    songs.html template.
    """

    def get(self, request, *args, **kwargs):
        """
        Gets all of the songs if the user is the super user, else it finds
        the superuser's username and gets all the songs by them (all Pre-made
        songs).
        Gets all of the genres from the Genres model.
        Sets any potentially unused variables as None by default to avoid
        errors in the template.
        """
        if request.user.is_superuser:
            songs = Song.objects.all()
        else:
            # pre-made songs = admin is the user
            superuser_name = User.objects.get(is_superuser=True)
            premade_songs = Song.objects.filter(user=superuser_name)
            # filtering these songs by only public ones
            songs = premade_songs.filter(public=True)

        genres = Genre.objects.all()

        query = None
        sort = None
        direction = None
        selected_genre = None
        selected_genre_display_name = None

        # ----------- credit- CI walkthrough for how to implement this
        # checking if sorting has been applied first
        # https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/products/views.py
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            # using 'annotation' to add temporary field to model
            if sort_key == 'name':
                sort_key = 'lower_name'
                songs = songs.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'

            # ordering the songs
            songs = songs.order_by(sort_key)

        # if query (name attribute on search form input) exists
        # we need to get its value
        if 'query' in request.GET:
            query = request.GET['query']
            # handling blank search with django message and redirect
            if not query:
                # include error message with django messages
                messages.error(request, "Your query is empty")
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
            genre = Genre.objects.get(name=selected_genre)
            selected_genre_display_name = genre.display_name
            songs = songs.filter(genre=genre.pk)

        all_users_bought_songs = []
        if self.request.user.is_authenticated:
            # gets all of the user's Orders
            users_orders = Order.objects.filter(
                user_profile=self.request.user.id
            )
            # loops through all orders and appends all order songs to the list
            for order in users_orders:
                order_songs = OrderSong.objects.filter(order=order)
                for song in order_songs:
                    the_songs = list(Song.objects.filter(id=song.song.id))
                    for song in the_songs:
                        all_users_bought_songs.append(song)

        context = {
            'songs': songs,
            'song_search': query,
            'sort_parameters': selected_sorting,
            'genres': genres,
            'selected_genre': selected_genre,
            'selected_genre_display_name': selected_genre_display_name,
            'all_users_bought_songs': all_users_bought_songs,
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

        # getting the song's associated instruments
        instruments = SongInstrument.objects.filter(song=song)

        # setting like as False until its confirmed it has likes
        like = False
        if song.likes.filter(id=self.request.user.id).exists():
            like = True

        # if the user is logged in, then it checks if they have
        # already ordered a song
        user_has_bought_song = False
        if self.request.user.is_authenticated:
            # getting all the OrderSong instance for the song
            all_songs_orders = OrderSong.objects.filter(song=song)

            # gets all of the user's Orders
            users_orders = Order.objects.filter(
                user_profile=self.request.user.id
            )

            # loop through their orders
            for order in users_orders:
                if all_songs_orders.filter(order=order).exists():
                    user_has_bought_song = True

        context = {
            'song': song,
            'like': like,
            'instruments': instruments,
            'user_has_bought_song': user_has_bought_song,
        }

        return render(request, 'songs/song_details.html', context)


# based on the 'chef's kisses' from my Potfolio 4 Project - Cook eBook
# credit - https://github.com/mountaincharlie/project-four-cook-ebook/blob/main/cook_ebook/views.py
class LikeSong(View):
    """
    Class based view inheriting Django's View
    Contains the post method for changing the like icon and
    likes count in the song's song_details page when the
    user clicks the like button.
    """

    def post(self, request, *args, **kwargs):
        """
        post method for when authenticated users click on song's like button.
        -gets the song by its unique slug
        -if statement for finding if the user's id already exists for
        this song's likes field
        -if the user exists then it removes the user
        -else it adds the user
        -returns the redirect of the song's absolute url
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])

        if song.likes.filter(id=request.user.id).exists():
            song.likes.remove(request.user)
        else:
            song.likes.add(request.user)

        return redirect(song.get_absolute_url())


class TestimonialsList(generic.ListView):
    """
    Class based view inheriting Django's generic.ListView
    Uses the Song model to find all the songs with use_as_testimonial = True
    and returns them to the testimonials.html template.
    """

    def get(self, request, *args, **kwargs):
        """
        Gets all of the songs which have use_as_testimonial=True.
        If the request user is not the superuser, then all the testimonials
        songs are filtered to only get the public ones since.
        The 'no_testimonial_text' variable contains a short message to
        display if the user doesn't provide any testimonial text.
        (By passing it into the template via the context, I can use a
        template tag filter to truncate it at a certain number of characters)
        """
        testimonial_songs = Song.objects.filter(use_as_testimonial=True)

        if request.user.is_superuser is False:
            testimonial_songs = testimonial_songs.filter(public=True)

        no_testimonial_text = 'This song has been chosen as an example of what midiDRAGON is able to create for our users.'

        context = {
            'songs': testimonial_songs,
            'no_testimonial_text': no_testimonial_text,
        }

        return render(request, "songs/testimonials.html", context)


class DesignCustomSong(View):
    """
    Class based view inheriting Django's View
    Contains the get method for displaying the form to design a custom
    song in the Design Custom Song template.
    Contains the post method for taking in the data submitted in the form
    to create the instance of Song in the database if the form is valid.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for getting the forms to be displayed to the user.
        if the super user tries to view this page it redirects them
        to their Site Management page
        -gets the DesignCustomSongForm and AddSongInstrumentFormSet
        -gets all instruments for the dropdown selection displayed
        to users
        -gets all the project_types to handle user's selection in
        the form
        -gets the MAX_NUM_REVIEW_SESSIONS var from settings.py
        -gets the ADDITIONAL_INSTRUMENT_PRICE var from settings.py
        -gets the ADDITIONAL_REVIEW_SESSION_PRICE var from settings.py
        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

        custom_song_form = DesignCustomSongForm()
        song_instrument_formset = AddSongInstrumentFormSet()

        instruments = Instrument.objects.all()
        project_types = ProjectType.objects.all()

        max_num_review_sessions = settings.MAX_NUM_REVIEW_SESSIONS
        additional_instrument_price = settings.ADDITIONAL_INSTRUMENT_PRICE
        additional_review_session_price = settings.ADDITIONAL_REVIEW_SESSION_PRICE

        context = {
            'custom_song_form': custom_song_form,
            'song_instrument_formset': song_instrument_formset,
            'instruments': instruments,
            'project_types': project_types,
            'max_num_review_sessions': max_num_review_sessions,
            'additional_instrument_price': additional_instrument_price,
            'additional_review_session_price': additional_review_session_price,
        }

        return render(request, 'songs/design_custom_song.html', context)

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the save button, which
        submits the design custom song forms.
        -gets the submitted form instance
        -if its valid, the song is created from the data and the request
        user is applied as the user for the song
        -gets the instance of AddSongInstrumentFormSet for the new song
        -if that is valid it is saved, a success message is displayed
        and the user is taken to the newly created song.
        -if the form isnt valid, a message is displayed to the user and
        they are taken back to the form.
        """

        custom_song_form = DesignCustomSongForm(request.POST, request.FILES)

        if custom_song_form.is_valid():
            song = custom_song_form.save(commit=False)
            song.user = User.objects.get(id=self.request.user.id)
            song.save()

            instruments_formset = AddSongInstrumentFormSet(
                request.POST, instance=song
            )

            if instruments_formset.is_valid():
                instruments_formset.save()

            messages.success(
                request,
                (f'"{song.name}" project was successfully created!')
            )
            return redirect(song.get_absolute_url())

        else:
            messages.error(
                request,
                ('Please ensure all the required form fields have been correctly filled in.')
            )
            context = {
                'custom_song_form': custom_song_form,
            }
            return render(request, 'songs/design_custom_song.html', context)


class EditCustomSong(View):
    """
    Class based view inheriting Django's View
    Contains the get method for displaying the form to edit a custom
    song in the edit Custom Song template.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for getting the prepopulated forms to be displayed to the
        user
        -gets the song to be edited
        -gets all associated song instruments
        -gets the forms and pre-populates them with the song instance
        -gets all instruments for the dropdown selection displayed to users
        -gets all the project_types to handle user's selection in the form
        -gets the MAX_NUM_REVIEW_SESSIONS var from settings.py
        -gets the ADDITIONAL_INSTRUMENT_PRICE var from settings.py
        -gets the ADDITIONAL_REVIEW_SESSION_PRICE var from settings.py
        -get the existing number of reviews to pre-pop the form
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        song_instruments = SongInstrument.objects.filter(song=song)

        custom_song_form = DesignCustomSongForm(instance=song)
        song_instrument_formset = AddSongInstrumentFormSet(instance=song)

        instruments = Instrument.objects.all()
        project_types = ProjectType.objects.all()

        max_num_review_sessions = settings.MAX_NUM_REVIEW_SESSIONS
        additional_instrument_price = settings.ADDITIONAL_INSTRUMENT_PRICE
        additional_review_session_price = settings.ADDITIONAL_REVIEW_SESSION_PRICE

        num_existing_review_sessions = song.num_of_reviews

        context = {
            'song': song,
            'custom_song_form': custom_song_form,
            'song_instrument_formset': song_instrument_formset,
            'instruments': instruments,
            'project_types': project_types,
            'max_num_review_sessions': max_num_review_sessions,
            'additional_instrument_price': additional_instrument_price,
            'additional_review_session_price': additional_review_session_price,
            'song_instruments': song_instruments,
            'num_existing_review_sessions': num_existing_review_sessions,
        }

        return render(request, 'songs/edit_custom_song.html', context)

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the save button, which
        submits the design custom song forms.
        -gets the song which has been edited
        -gets the form with the song instance
        -if the form is valid the song is updated and saved
        -gets AddSongInstrumentFormSet
        -if its valid, it removes existing song instruments for
        this song so that only the new are applied
        -a success message is displayed
        -if the form isnt valid then the user is taken back to
        the form and an error message is displayed
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        custom_song_form = DesignCustomSongForm(
            request.POST,
            request.FILES,
            instance=song
        )

        if custom_song_form.is_valid():
            song = custom_song_form.save(commit=False)
            song.user = User.objects.get(id=self.request.user.id)
            song.save()

            instruments_formset = AddSongInstrumentFormSet(
                request.POST, instance=song
            )

            if instruments_formset.is_valid():
                instruments_to_delete = SongInstrument.objects.filter(song=song).delete()

                instruments_formset.save()

            messages.success(
                request,
                (f'"{song.name}" project was successfully updated!')
            )
            return redirect(song.get_absolute_url())

        else:
            messages.error(
                request,
                ('Please ensure all the required form fields have been correctly filled in.')
            )
            context = {
                'custom_song_form': custom_song_form,
            }
            return render(request, 'songs/edit_custom_song.html', context)


class DeleteSong(generic.DeleteView):
    """
    DeleteSong class based view inheriting Django's
    generic.DeleteView
    FINISH ...
    """
    model = Song
    template_name = "songs/delete_song.html"

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the Delete button in the Delete
        Song page, which is for confirming the user wants to delete the
        song.
        -gets the song by its unique slug
        -deletes the song from the database
        -a custom success message is passed into django messages.success along
        with request
        -the user is then redirected to their profile
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])

        # if request.user.is_superuser => delete
        if request.user.is_superuser:
            song.delete()
            messages.success(
                request,
                (f'"{song.name}" was successfully deleted')
            )
            return render(
                request,
                'home/index.html'
            )
        elif request.user.username == song.user.username:
            song.delete()
            messages.success(
                request,
                (f'"{song.name}" was successfully deleted')
            )
            return render(request, 'home/index.html')
        else:
            messages.error(
                request,
                ('You do not have permission to make this action')
            )
            return render(request, 'home/index.html')
