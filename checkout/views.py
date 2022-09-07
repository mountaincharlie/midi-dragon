"""
View functions and classes to handle the checkout app functionality

CREDITS - in README
-Views based on the logic from the CI walkthrough view functions and adapted
for this project.
-Creating the PaymentIntent using auto payment menthods in python from the
Stripe docs
"""
import json
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.conf import settings
from tracklist.contexts import tracklist_contents
from songs.models import Song
from .models import Order, OrderSong
from .forms import OrderForm


@require_POST
def cache_checkout_data(request):
    """
    Function to pass customer information through a stripe payment intent as
    metadata (creating a cache of the tracklist data for the webhook handling)
    -Uses a Try/Except block
    -Gets the payment_intent id from the first part of the 'client_secret'
    -Sets up stripe with api key from settings.py variable
    -Call the modify method on the PaymentIntent with metadata for
    username and a json dump of the entire tracklist
    -Returns a status 200 httpresponse
    -If there are any errors then a message is displayed to the user and a
    status 400 httpresponse is returned
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'tracklist': json.dumps(request.session.get('tracklist', [])),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment could not be processed \n at this time please try again later. \n If the issue persists, please contact midiDRAGON')
        return HttpResponse(content=e, status=400)


class CheckoutView(View):
    """
    Class based view inheriting Django's View
    Uses the Order model for rendering the OrderForm in the
    checkout.html template.
    -Sets the stripe_public_key and stripe_secret_key
    -Contains the get method for displaying the form to the user
    -Contains the post method for handling the form submission posted
    from stripe_elements.js which handles the form submission
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    def get(self, request, *args, **kwargs):
        """
        -First checks if the user is trying to manually view the checkout
        and redirects them to their All Songs page if so.
        -Gets the tracklist list from the session
        -Includes a check in case the user tries to manually access the
        checkout through the url when they dont have anything in their
        tracklist
        -If their tracklist is empty then a message is displayed to them
        and theyre redirected to the pre-made songs browsing page
        -Sets the current_tracklist from the tracklist_contents() in
        tracklist/contexts.py
        -Gets the tracklist_total for the current_tracklist
        -Gets stripe_total as an integer as Stripe requires this
        -Sets stripe.api_key as our stripe_secret_key
        -Creates the PaymentIntent (dictionary of details about the payment)
        credit in this file's docstring
        -If the user is logged in, their instance of the User model is used
        to prepopulate the full_name and email fields (they're still editable)
        otherwise just an empty instance of OrderForm is sent to the template
        """

        if request.user.is_superuser:
            messages.info(request, "Admin redirected to Site Management page.")
            return redirect(reverse('all_songs'))

        tracklist = request.session.get('tracklist', [])

        if not tracklist:
            messages.error(request, 'You cannot checkout since there are currently no items in your tracklist')
            return redirect(reverse('songs'))

        current_tracklist = tracklist_contents(request)
        tracklist_total = current_tracklist['tracklist_total']
        stripe_total = round(tracklist_total * 100)
        stripe.api_key = self.stripe_secret_key

        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # checking if the user is authenticated and prepoping their data if
        if request.user.is_authenticated:
            try:
                profile = User.objects.get(id=self.request.user.id)
                order_form = OrderForm(initial={
                    'full_name': profile.get_full_name(),
                    'email': profile.email,
                })
            except User.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)

    def post(self, request, *args, **kwargs):
        """
        -Gets the tracklist list from the session or creates an empty list if
        it doesn't exist
        -Creates a dictionary of form data as teh instance of the form since
        its submission is handled in stripe_elmenets.js
        -Sets order_form = the OrderForm instance
        -If the form is valid, the order is saved but not committed, the
        payment intent id (pid) is taken from the first part of the
        'client_secret'
        -Sets the order's paymentIntent id (pid) and original_tracklist with
        a json dump of the tracklist from the session
        -Saves the order
        -Iterates through the song objects in the tracklist list to create
        each OrderSong instance, using a Try/Except block to check that the
        song exists
        -If it doesn't exist anymore, a message is displayed to the user, the
        order is deleted and the user is redirected to their Tracklist
        -If it deos exist, then after creating and saving it, the user is
        redirected to the order_confirmation page.
        -If the form is invalid, a message is displayed to the user and the
        checkout page is reloaded with the data that was posted by the user
        """
        tracklist = request.session.get('tracklist', [])

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]

            order.stripe_pid = pid
            order.original_tracklist = json.dumps(tracklist)
            order.save()

            for song in tracklist:
                try:
                    existing_song = Song.objects.get(slug=song)
                    order_song = OrderSong(
                            order=order,
                            song=existing_song,
                        )
                    order_song.save()
                except Song.DoesNotExist:
                    messages.error(request, (
                        f'"{song}" was not found in our database.'
                        'Please contact midiDRAGON for assistance.'
                        ))
                    order.delete()
                    return redirect(reverse('tracklist'))

            return redirect(reverse(
                'order_confirmation', args=[order.order_number]
                ))
        else:
            messages.error(request, (
                'There was an error processing your order form. \n Please ensure all your details have been correctly filled out.'
            ))

        client_secret = request.POST.get('client_secret')
        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': client_secret,
        }

        return render(request, 'checkout/checkout.html', context)


class OrderConfirmation(View):
    """
    Class based view inheriting Django's View
    view to handle successful checkouts
    -Contains the get method for displaying the Order overview to the user
    """
    def get(self, request, *args, **kwargs):
        """
        -Takes in the request and the order_number for the order just created
        -Gets the order by its number
        -Gets the order's associated songs
        -If the user is logged in then it adds their profile to the order
        instance
        -Displays a success message to the user with the order number and the
        email that the confirmation will be sent to
        -Clears the tracklist from the session
        -Passes the order instance through the context
        -return renders the order_confirmation page
        """
        order = get_object_or_404(
            Order,
            order_number=self.kwargs['order_number']
        )

        songs = OrderSong.objects.filter(order=order)

        if request.user.is_authenticated:
            profile = User.objects.get(id=request.user.id)
            order.user_profile = profile
            order.save()

        messages.success(request, f'Your order was successful placed! \n Order number: {order.order_number}. \n A confirmation email will be sent to {order.email}')

        if 'tracklist' in request.session:
            del request.session['tracklist']

        context = {
            'order': order,
            'songs': songs,
        }

        return render(request, 'checkout/order_confirmation.html', context)
