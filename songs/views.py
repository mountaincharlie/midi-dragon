import os
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from django.db.models import Q
from django.db.models.functions import Lower
from django.conf import settings
from django.http import HttpResponse
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
        // FINISH
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
            # print('select value?', selected_genre)
            genre = Genre.objects.get(name=selected_genre)
            selected_genre_display_name = genre.display_name
            # print('selected genre:', genre.pk)
            songs = songs.filter(genre=genre.pk)

        all_users_bought_songs = []
        if self.request.user.is_authenticated:
            # gets all of the user's Orders
            users_orders = Order.objects.filter(user_profile=self.request.user.id)
            # loops through all orders and appends all order songs to the list
            for order in users_orders:
                order_songs = OrderSong.objects.filter(order=order)
                print('order_songs', order_songs)
                for song in order_songs:
                    the_songs = list(Song.objects.filter(id=song.song.id))
                    print('the_songs', the_songs)
                    for song in the_songs:
                        all_users_bought_songs.append(song)
                        print('all_users_bought_songs', all_users_bought_songs)


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

        # if the user is logged in, then it checks if they have already ordered a song
        user_has_bought_song = False
        if self.request.user.is_authenticated:
            # getting all the OrderSong instance for the song
            all_songs_orders = OrderSong.objects.filter(song=song)
            print('all of the songs order', all_songs_orders)

            # gets all of the user's Orders
            users_orders = Order.objects.filter(user_profile=self.request.user.id)
            print('all of the users_orders users_orders', list(users_orders))

            # loop through their orders
            for order in users_orders:
                print('order:', order)
                if all_songs_orders.filter(order=order).exists():
                    print('theyve ordered the song before')
                    user_has_bought_song = True
                else:
                    print('theyve NOT bought the song')

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
        FINISH...
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        filename = str(song.audio_file)
        if 'USE_AWS' in os.environ:
            # file_path = f'{settings.MEDIA_URL}'+filename
            # file_path = 'https://mididragon.s3.eu-west-2.amazonaws.com/media/'+filename
            import boto3

            client = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_S3_REGION_NAME
            )
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            file_name = settings.MEDIAFILES_LOCATION + '/' + filename
            s3 = boto3.resource('s3')

            url = client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_name, },
                ExpiresIn=600, )

            s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).download_file(filename, url)
            #ABOVE WORKS BUT NOT IDEAL

            # return HttpResponseRedirect(url)
            # import boto3

            # session = boto3.Session(
            #     aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            #     aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            #     region_name=settings.AWS_S3_REGION_NAME
            # )

            # s3 = session.resource('s3')

            # file_path = 'https://mididragon.s3.eu-west-2.amazonaws.com/media/' + filename

            # s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).download_file(filename, file_path)

            # import boto3

            # BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
            # KEY = 'media/' + filename

            # s3 = boto3.resource('s3')

            # s3.Bucket(BUCKET_NAME).download_file(KEY, 'download.mp3')

            # import boto3

            # s3_client = boto3.client(
            #     's3',
            #     aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            #     aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            #     region_name=settings.AWS_S3_REGION_NAME
            # )

            # file_path = 'https://mididragon.s3.eu-west-2.amazonaws.com/media/' + filename

            # s3_client.download_file(settings.AWS_STORAGE_BUCKET_NAME, filename, file_path)

            return render(request, "home/index.html")

        else:
            file_path = 'media/'+filename
        mime_type = filename.split('.')[1]

        # logic for opening the file and allowing it to be downloaded from adapted from (CREDIT - https://djangoadventures.com/how-to-create-file-download-links-in-django/)
        read_file = open(file_path, 'rb')
        response = HttpResponse(read_file, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response


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
        -gets the
        FINISH ...

        """
        custom_song_form = DesignCustomSongForm()
        song_instrument_formset = AddSongInstrumentFormSet()

        # gets all instruments for the dropdown selection displayed to users
        instruments = Instrument.objects.all()

        # gets all the project_types to handle user's selection in the form
        project_types = ProjectType.objects.all()

        # gets the MAX_NUM_REVIEW_SESSIONS var from settings.py
        max_num_review_sessions = settings.MAX_NUM_REVIEW_SESSIONS
        # gets the ADDITIONAL_INSTRUMENT_PRICE var from settings.py
        additional_instrument_price = settings.ADDITIONAL_INSTRUMENT_PRICE
        # gets the ADDITIONAL_REVIEW_SESSION_PRICE var from settings.py
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
        -gets 
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
    FINISH ...
    """

    def get(self, request, *args, **kwargs):
        """
        get method for getting the prepopulated forms to be displayed to the
        user
        -gets the
        FINISH ...
        """

        # gets the song to be edited
        song = get_object_or_404(Song, slug=self.kwargs['slug'])

        # gets all associated song instruments 
        song_instruments = SongInstrument.objects.filter(song=song)


        # gets the forms and pre-populates them with the song instance
        custom_song_form = DesignCustomSongForm(instance=song)
        song_instrument_formset = AddSongInstrumentFormSet(instance=song)
        # print(song_instrument_formset)

        # gets all instruments for the dropdown selection displayed to users
        instruments = Instrument.objects.all()

        # gets all the project_types to handle user's selection in the form
        project_types = ProjectType.objects.all()

        # gets the MAX_NUM_REVIEW_SESSIONS var from settings.py
        max_num_review_sessions = settings.MAX_NUM_REVIEW_SESSIONS
        # gets the ADDITIONAL_INSTRUMENT_PRICE var from settings.py
        additional_instrument_price = settings.ADDITIONAL_INSTRUMENT_PRICE
        # gets the ADDITIONAL_REVIEW_SESSION_PRICE var from settings.py
        additional_review_session_price = settings.ADDITIONAL_REVIEW_SESSION_PRICE

        # getting the existing number of reviews to pre-pop the form
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
        -gets 
        FINISH ...
        """
        # gets the song which has been edited
        song = get_object_or_404(Song, slug=self.kwargs['slug'])

        # gets the form with the song instance
        custom_song_form = DesignCustomSongForm(request.POST, request.FILES, instance=song)

        # if request.FILES.get('upload_image'):
        #     song.image = request.FILES.get('upload_image')
        #     song.save()

        if custom_song_form.is_valid():
            song = custom_song_form.save(commit=False)
            song.user = User.objects.get(id=self.request.user.id)
            # check if image stays correct
            song.save()

            instruments_formset = AddSongInstrumentFormSet(
                request.POST, instance=song
            )

            if instruments_formset.is_valid():
                # removing existing song instruments for this song so that only the new are applied
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
            messages.success(request, (f'"{song.name}" was successfully deleted'))
            return render(request, 'home/index.html')
            # return redirect()  # REDIRECT TO PROFILE once app created

        # ADD --- AND doesnt exist in an order (hasnt been bought yet) => delete
        elif request.user.username == song.user.username:
            song.delete()
            messages.success(request, (f'"{song.name}" was successfully deleted'))
            return render(request, 'home/index.html')
            # return redirect()  # REDIRECT TO PROFILE once app created
        else:
            messages.error(request, ('You do not have permission to make this action'))
            return render(request, 'home/index.html')
