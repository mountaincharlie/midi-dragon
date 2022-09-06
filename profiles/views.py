from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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
        # if the super user tries to view this page it redirects them to their Site Management page
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management page.")
            return redirect(reverse('all_songs'))

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
        # if the super user tries to view this page it redirects them to their Site Management page
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management page.")
            return redirect(reverse('all_songs'))

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
                    song = list(song)[0]  # getting the actual song out of the q set
                    if song in users_custom_songs:
                        print('users_custom_songs before', users_custom_songs)
                        users_custom_songs.remove(song)  # using remove rather than pop which is for integers
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
        # if the super user tries to view this page it redirects them to their Site Management page
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management page.")
            return redirect(reverse('all_songs'))

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
        # if the super user tries to view this page it redirects them to their Site Management page
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management page.")
            return redirect(reverse('all_songs'))

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
        # if the super user tries to view this page it redirects them to their Site Management page
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management page.")
            return redirect(reverse('all_songs'))

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


class OrderOverview(View):
    """
    Class based view inheriting Django's View
    view to handle successful checkouts
    -Contains the get method for displaying the Order overview to the user
    """
    def get(self, request, *args, **kwargs):
        """
        -Takes in the request and the order_number for the order
        -Gets the order by its number
        -Gets the order's associated songs
        -Passes the order instance and order_songs through the context
        -return renders the order_overview page
        """
        order = get_object_or_404(Order, order_number=self.kwargs['order_number'])

        order_songs = OrderSong.objects.filter(order=order)

        context = {
            'order': order,
            'order_songs': order_songs,
        }

        return render(request, 'profiles/order_overview.html', context)


class AllSongsAdminView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # checks that it is the admin who is the logged in user rtying to access the page, else redirects the user with a message
        if not request.user.is_superuser:
            messages.error(request, "You don't have access to this page.")
            return redirect(reverse('home'))

        # resetting all filter vars
        selected_song_type = None
        selected_user = None
        selected_done_status = None
        selected_public_status = None
        selected_testimonial_status = None

        # gets all of the songs in the db
        all_songs = Song.objects.all()

        # gets all of the users
        all_users = User.objects.all()

        # checking if the Song type filter has been applied
        if 'songtype' in request.GET:
            selected_song_type = request.GET['songtype']
            superuser = get_object_or_404(User, is_superuser=True)
            if selected_song_type == 'pre-made':
                print('PRE-MADE, admin:', superuser)
                all_songs = all_songs.filter(user=superuser)
            elif selected_song_type == 'custom':
                # CREDIT using negate filter ~Q 
                all_songs = all_songs.filter(~Q(user=superuser))

        # checking if the User filter has been applied
        if 'songuser' in request.GET:
            selected_user = str(request.GET['songuser'])
            user = get_object_or_404(User, username=selected_user)
            all_songs = all_songs.filter(user=user)

        # checking if the done status filter has been applied
        if 'donestatus' in request.GET:
            selected_done_status = request.GET['donestatus']
            if selected_done_status == 'done':
                all_songs = all_songs.filter(completed=True)
            elif selected_done_status == 'not-done':
                all_songs = all_songs.filter(completed=False)

        # checking if the public status filter has been applied
        if 'publicstatus' in request.GET:
            selected_public_status = request.GET['publicstatus']
            if selected_public_status == 'public':
                all_songs = all_songs.filter(public=True)
            elif selected_public_status == 'private':
                all_songs = all_songs.filter(public=False)

        # checking if the testimonial status filter has been applied
        if 'testimonialstatus' in request.GET:
            selected_testimonial_status = request.GET['testimonialstatus']
            if selected_testimonial_status == 'testimonial':
                all_songs = all_songs.filter(use_as_testimonial=True)
            elif selected_testimonial_status == 'not-testimonial':
                all_songs = all_songs.filter(use_as_testimonial=False)

        # returns all custom and pre-made songs
        context = {
            'all_songs': all_songs,
            'all_users': all_users,
            'selected_song_type': selected_song_type,
            'selected_user': selected_user,
            'selected_done_status': selected_done_status,
            'selected_public_status': selected_public_status,
            'selected_testimonial_status': selected_testimonial_status,
        }

        return render(request, 'profiles/site_management_all_songs.html', context)


class AllOrdersAdminView(View):
    """
    Class based view inheriting Django's View
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # checks that it is the admin who is the logged in user rtying to access the page, else redirects the user with a message
        if not request.user.is_superuser:
            messages.error(request, "You don't have access to this page.")
            return redirect(reverse('home'))

        # resetting all filter vars
        selected_user = None
        selected_date_order = None

        # gets all of the songs in the db
        all_orders = Order.objects.all()

        # gets all of the users
        all_users = list(User.objects.all())

        # checking if the User filter has been applied
        if 'orderuser' in request.GET:
            selected_user = str(request.GET['orderuser'])
            if selected_user == 'anonymous':
                user = None
            else:
                user = get_object_or_404(User, username=selected_user)
            all_orders = all_orders.filter(user_profile=user)
        
        # checking if the date ordering has been applied
        if 'dateorder' in request.GET:
            selected_date_order = request.GET['dateorder']
            order_key = 'date'
            if selected_date_order == 'newest':
                order_key = f'-{order_key}'
            # ordering the orders
            all_orders = all_orders.order_by(order_key)

        # returns all orders
        context = {
            'all_orders': all_orders,
            'all_users': all_users,
            'selected_user': selected_user,
            'selected_date_order': selected_date_order,
        }

        return render(request, 'profiles/site_management_all_orders.html', context)
