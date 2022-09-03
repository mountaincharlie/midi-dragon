from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from checkout.models import Order, OrderSong
from songs.models import Song
from .forms import MyDetailsForm


class MyDetailsView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    MAKE A CLASS BASED VIEW?
    """
    def get(self, request, *args, **kwargs):
        """
        get method for getting the forms to be displayed to the user.
        -gets the
        FINISH ...

        """
        # gets the MyDetailsForm() with the users details if possible
        try:
            my_details_form = MyDetailsForm(initial={
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email,
            })
        except Exception as e:
            my_details_form = MyDetailsForm()
            print('didnt work:', e)
            return HttpResponse(content=e, status=400)

        context = {
            'my_details_form': my_details_form,
        }

        return render(request, 'profiles/dashboard_my_details.html', context)

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the save button, which
        submits the my details forms.
        -gets
        """
        # gets the user who is being edited
        user = self.request.user

        # gets the form with the song instance
        my_details_form = MyDetailsForm(request.POST, instance=user)
        print('my_details_form', my_details_form)

        if my_details_form.is_valid():
            user = my_details_form.save(commit=False)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            messages.success(
                request,
                (f'Your details were successfully updated {self.request.user.first_name} {self.request.user.last_name}!')
            )
            context = {
                'my_details_form': my_details_form,
            }
            return render(request, 'profiles/dashboard_my_details.html', context)

        else:
            messages.error(
                request,
                ('Please ensure all the required form fields have been correctly filled in.')
            )
            context = {
                'my_details_form': my_details_form,
            }
            return render(request, 'profiles/dashboard_my_details.html', context)


class ProjectDraftsView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # gets all the user's custom songs (filter songs by user = self.request.user) AS A LIST
        users_custom_songs = list(Song.objects.filter(user=self.request.user.id))
        print('users_custom_songs', users_custom_songs)

        # gets all of the user's Orders
        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        # loops through all orders and appends all order songs to the list
        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            print('order_songs', order_songs)
            the_songs = []
            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))
                print('the_songs', the_songs)
                for song in the_songs:
                    # all_users_bought_songs.append(song)
                    if song in users_custom_songs:
                        print('users_custom_songs before', users_custom_songs)
                        users_custom_songs.pop(song)
                        print('users_custom_songs after', users_custom_songs)
                    else:
                        print('this song is a purchased pre-made song or a unpurchased custom song', song)

        # returns the users unpurchased custom songs
        context = {
            'unpurchased_users_custom_songs': users_custom_songs,
        }

        return render(request, 'profiles/dashboard_project_drafts.html', context)


class ProjectsInProgressView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # defines the list for incomplete purchased custom songs created belonging to the user
        users_incomplete_purchased_custom_songs = {}

        # gets all of the user's Orders
        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        # loops through all orders and appends all order songs to the list
        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            print('order_songs', order_songs)
            the_songs = []
            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))
                print('the_songs', the_songs)
                for song in the_songs:
                    song = song[0]
                    # if the song is a custom song and not complete
                    if song.user == self.request.user and not song.completed:
                        # adds the song as a key and its order as the value
                        users_incomplete_purchased_custom_songs[song] = order
                    else:
                        print('this song is a purchased pre-made song or a unpurchased custom song', song)

        # print(type(users_custom_songs[0]))
        # returns the users unpurchased custom songs
        context = {
            'users_incomplete_purchased_custom_songs': users_incomplete_purchased_custom_songs,
        }

        return render(request, 'profiles/dashboard_projects_in_progress.html', context)


class CompletedProjectsView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # defines the list for complete purchased custom songs created belonging to the user
        users_complete_purchased_custom_songs = {}

        # gets all of the user's Orders
        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        # loops through all orders and appends all order songs to the list
        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            print('order_songs', order_songs)
            the_songs = []
            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))
                print('the_songs', the_songs)
                for song in the_songs:
                    song = song[0]
                    # if the song is a custom song and are complete
                    if song.user == self.request.user and song.completed:
                        # adds the song as a key and its order as the value
                        users_complete_purchased_custom_songs[song] = order
                    else:
                        print('this song is a purchased pre-made song or a unpurchased custom song', song)

        context = {
            'users_complete_purchased_custom_songs': users_complete_purchased_custom_songs,
        }

        return render(request, 'profiles/dashboard_completed_projects.html', context)


class OrderHistoryView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # gets all of the user's Orders
        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        users_orders_dict = {}

        # creates a dictionary with Orders as keys and a list of their songs as the value
        for order in users_orders:
            order_songs = list(OrderSong.objects.filter(order=order))
            users_orders_dict[order] = order_songs

        context = {
            'users_orders_dict': users_orders_dict,
        }

        return render(request, 'profiles/dashboard_order_history.html', context)
