""" view.py for the profiles app """
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
    """
    def get(self, request, *args, **kwargs):
        """
        -if the super user tries to view this page it redirects them to
        their Site Management page
        get method for getting the forms to be displayed to the user.
        -gets the MyDetailsForm() with the users details if possible

        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

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
        -gets the user who is being edited
        -gets the form with the song instance
        -updates the user model with the form values if the form is
        valid and redirects back to My Details bage with success message.
        -if the form is invalid the user is setn an error message
        """
        user = self.request.user

        my_details_form = MyDetailsForm(request.POST, instance=user)

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
            return render(
                request,
                'profiles/dashboard_my_details.html',
                context
            )

        else:
            messages.error(
                request,
                ('Please ensure all the required form fields have been correctly filled in.')
            )
            context = {
                'my_details_form': my_details_form,
            }
            return render(
                request,
                'profiles/dashboard_my_details.html',
                context
            )


class ProjectDraftsView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -if the super user tries to view this page it redirects them
        to their Site Management page
        -gets all the user's custom songs (filter songs by user =
        self.request.user) as a list
        -gets all of the user's Orders
        -loops through all orders and appends all order songs to the
        list
        -for each object in that list it gets the actualy song out of
        the query set
        -if the song is in the users_custom_songs then it gets removed
        -context contains the users unpurchased custom songs to pass
        into the template
        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

        users_custom_songs = list(
            Song.objects.filter(
                user=self.request.user.id
                )
            )

        users_orders = Order.objects.filter(user_profile=self.request.user.id)

        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            the_songs = []

            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))

                for song in the_songs:
                    song = list(song)[0]

                    if song in users_custom_songs:
                        users_custom_songs.remove(song)

        context = {
            'unpurchased_users_custom_songs': users_custom_songs,
        }

        return render(
            request,
            'profiles/dashboard_project_drafts.html',
            context
        )


class ProjectsInProgressView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -if the super user tries to view this page it redirects them
        to their Site Management page
        -defines the list for incomplete purchased custom songs created
        belonging to the user
        -gets all of the user's Orders
        -loops through all orders and appends all order songs to the list
        -for each song object in the list, it gets its actual song
        -if the song is a custom song and not complete, it adds the
        song as a key and its order as the value
        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

        users_incomplete_purchased_custom_songs = {}

        users_orders = Order.objects.filter(user_profile=self.request.user.id)

        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            print('order_songs', order_songs)
            the_songs = []

            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))

                for song in the_songs:
                    song = song[0]
                    if song.user == self.request.user and not song.completed:
                        users_incomplete_purchased_custom_songs[song] = order

        context = {
            'users_incomplete_purchased_custom_songs': users_incomplete_purchased_custom_songs,
        }

        return render(
            request,
            'profiles/dashboard_projects_in_progress.html',
            context
        )


class CompletedProjectsView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -if the super user tries to view this page it redirects them to
        their Site Management page
        -defines the list for complete purchased custom songs created
        belonging to the user
        -gets all of the user's Orders
        -loops through all orders and appends all order songs to the
        list
        -if the song is a custom song and is complete, adds the song
        as a key and its order as the value
        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

        users_complete_purchased_custom_songs = {}

        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            the_songs = []
            for song in order_songs:
                the_songs.append(Song.objects.filter(id=song.song.id))
                print('the_songs', the_songs)
                for song in the_songs:
                    song = song[0]
                    if song.user == self.request.user and song.completed:
                        users_complete_purchased_custom_songs[song] = order

        context = {
            'users_complete_purchased_custom_songs': users_complete_purchased_custom_songs,
        }

        return render(
            request,
            'profiles/dashboard_completed_projects.html',
            context
        )


class OrderHistoryView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -if the super user tries to view this page it redirects them to
        their Site Management page
        -gets all of the user's Orders
        -defines a dictionary to store them in
        -creates a dictionary with Orders as keys and a list of their
        songs as the value
        """
        if request.user.is_superuser:
            messages.info(request, "Redirecting Admin to Site Management.")
            return redirect(reverse('all_songs'))

        users_orders = Order.objects.filter(user_profile=self.request.user.id)
        users_orders_dict = {}

        for order in users_orders:
            order_songs = list(OrderSong.objects.filter(order=order))
            users_orders_dict[order] = order_songs

        context = {
            'users_orders_dict': users_orders_dict,
        }

        return render(
            request,
            'profiles/dashboard_order_history.html',
            context
        )


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
        order = get_object_or_404(
            Order,
            order_number=self.kwargs['order_number']
        )

        order_songs = OrderSong.objects.filter(order=order)

        context = {
            'order': order,
            'order_songs': order_songs,
        }

        return render(request, 'profiles/order_overview.html', context)


class AllSongsAdminView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -checks that it is the admin who is the logged in user trying to access
        the page, else redirects the user with a message
        -resets all filter vars
        -gets all of the songs in the db
        -gets all of the users
        -checks if the Song type filter has been applied
        -if so it gets the 'songtype'
        -if the type is pre-made, then the songs are found by using the
        superuser
        -if the type is custom, then the songs are found by using
        ~Q(user=superuser) notation
        -checking if the User filter has been applied
        -if so, it gets the user, from the request and uses that string
        to get the user object and then filtering all the songs by
        this user
        -if the done status filter has been applied, then 'done' means
        filtering by completed=True and 'not done' means filtering by
        completed=False.
        -if the public status filter has been applied, then 'public'
        means filtering by public=True, else filtering by public=False
        -if the testimonial status filter has been applied, then
        'testimonial- means filtering the songs by use_as_testimonial=True
        """
        if not request.user.is_superuser:
            messages.error(request, "You don't have access to this page.")
            return redirect(reverse('home'))

        selected_song_type = None
        selected_user = None
        selected_done_status = None
        selected_public_status = None
        selected_testimonial_status = None

        all_songs = Song.objects.all()
        all_users = User.objects.all()

        if 'songtype' in request.GET:
            selected_song_type = request.GET['songtype']
            superuser = get_object_or_404(User, is_superuser=True)
            if selected_song_type == 'pre-made':
                all_songs = all_songs.filter(user=superuser)
            elif selected_song_type == 'custom':
                all_songs = all_songs.filter(~Q(user=superuser))

        if 'songuser' in request.GET:
            selected_user = str(request.GET['songuser'])
            user = get_object_or_404(User, username=selected_user)
            all_songs = all_songs.filter(user=user)

        if 'donestatus' in request.GET:
            selected_done_status = request.GET['donestatus']
            if selected_done_status == 'done':
                all_songs = all_songs.filter(completed=True)
            elif selected_done_status == 'not-done':
                all_songs = all_songs.filter(completed=False)

        if 'publicstatus' in request.GET:
            selected_public_status = request.GET['publicstatus']
            if selected_public_status == 'public':
                all_songs = all_songs.filter(public=True)
            elif selected_public_status == 'private':
                all_songs = all_songs.filter(public=False)

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

        return render(
            request,
            'profiles/site_management_all_songs.html',
            context
        )


class AllOrdersAdminView(View):
    """
    Class based view inheriting Django's View
    """
    def get(self, request, *args, **kwargs):
        """
        -checks that it is the admin who is the logged in user trying to
        access the page, else redirects the user with a message
        -resets all filter vars
        -gets all of the songs in the db
        -gets all of the users as a list
        -if the User filter has been applied, then it gets the user and
        filters the songs by them
        -if the date ordering has been applied, the order_key is set
        and its direction depends on whether the select value is 'newest'
        or 'oldest' and finally ordered the orders before passing them to
        the template
        """
        if not request.user.is_superuser:
            messages.error(request, "You don't have access to this page.")
            return redirect(reverse('home'))

        selected_user = None
        selected_date_order = None

        all_orders = Order.objects.all()
        all_users = list(User.objects.all())

        if 'orderuser' in request.GET:
            selected_user = str(request.GET['orderuser'])
            if selected_user == 'anonymous':
                user = None
            else:
                user = get_object_or_404(User, username=selected_user)
            all_orders = all_orders.filter(user_profile=user)

        if 'dateorder' in request.GET:
            selected_date_order = request.GET['dateorder']
            order_key = 'date'
            if selected_date_order == 'newest':
                order_key = f'-{order_key}'
            all_orders = all_orders.order_by(order_key)

        context = {
            'all_orders': all_orders,
            'all_users': all_users,
            'selected_user': selected_user,
            'selected_date_order': selected_date_order,
        }

        return render(
            request,
            'profiles/site_management_all_orders.html',
            context
        )
