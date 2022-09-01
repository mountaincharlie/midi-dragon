"""
Views based on the logic from the CI walkthrough view functions and adapted for this project
CREDIT - CI walkthrough [https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/views.py]
"""
import json
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
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
    function to pass customer information through a stripe payment intent as metadata (creating a cache of the tracklist data for the webhook handling)
    -gets the payment_intent id
    -sets up stripe with api key
    -call the modify method on the PaymentIntent with metadata for
    username and a json dump of the entire bag
    """
    #  tracklist is a list for creating orders, tracklist_json is a string used as the original_tracklist field
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            # 'tracklist_json': json.dumps(request.session.get('tracklist', [])),
            # 'tracklist': request.session.get('tracklist', []),
            'tracklist': json.dumps(request.session.get('tracklist', [])),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Sorry, your payment could not be processed \n at this time please try again later. \n If the issue persists, please contact midiDRAGON')
        return HttpResponse(content=e, status=400)


class CheckoutView(View):
    """
    Class based view inheriting Django's View
    Uses the Order model for rendering the OrderForm in the
    checkout.html template.
    """

    # stripe vars
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """
        # get tracklist list from the session
        tracklist = request.session.get('tracklist', [])

        # in case the user access the checkout page manually in the url
        # (since the secure checkout button is not avaliable in the tracklist
        # if the tracklist is empty)
        if not tracklist:
            messages.error(request, 'You cannot checkout since there are currently no items in your tracklist')
            return redirect(reverse('songs'))

        # sets the current_tracklist from the tracklist_contents() in tracklist/
        # contexts.py
        current_tracklist = tracklist_contents(request)
        # gets the tracklist_total for the current_tracklist
        tracklist_total = current_tracklist['tracklist_total']

        # stripe needs tracklist_total as an integer
        stripe_total = round(tracklist_total * 100)

        # setting stripe.api_key as our stripe_secret_key
        stripe.api_key = self.stripe_secret_key

        # creating the PaymentIntent (dict of details about the payment)
        # ------ CREDIT - https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements [Using auto payment menthods in python]
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # checking if the payment_intent works
        print('PAYMENT INTENT:', payment_intent)

        # checking if the user is authenticated and prepoping their data if
        # their profile can be found (USERPROFILE MODEL TO BE ADDED SOON)
        if request.user.is_authenticated:
            print('UserProfile data will be accessed once the app is created')
            order_form = OrderForm()
            # try:
            #     profile = UserProfile.objects.get(user=request.user)
            #     order_form = OrderForm(initial={
            #         'full_name': profile.user.get_full_name(),
            #         'email': profile.user.email,
            #     })
            # except UserProfile.DoesNotExist:
            #     order_form = OrderForm()
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
        -gets the bag from the session
        -if there is nothing in the bag an error message is displayed and the
        user is redirected to the products page
        -stores an instance of the OrderForm
        -defines the template to use
        -defines the context dict with the OrderForm to be accessed within
        the template
        FINISH ...
        """
        print('POST METHOD')
        # get tracklist list from the session
        tracklist = request.session.get('tracklist', [])

        # dict of data from the form (stores an instance of the OrderForm)
        # creating the form instance since the submit is handled with JS and we only want the full_name and email input values for our form [CREDIT - CI walkthrough]
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }

        order_form = OrderForm(form_data)

        # saving the form if its valid
        if order_form.is_valid():
            print('ORDER FORM IS VALID')
            order = order_form.save(commit=False)
            # the bit of client_secret before the '_secret' is the payment intent id
            pid = request.POST.get('client_secret').split('_secret')[0]

            # setting the order's paymentIntent id (pid)
            # and original_tracklist with a json dump of the tracklist from the session
            order.stripe_pid = pid
            order.original_tracklist = json.dumps(tracklist)
            order.save()

            # iterating through the song objects in the tracklist list
            # to create each OrderSong instance
            for song in tracklist:
                try:
                    # trying to get the song object from its slug (checking it still exists)
                    existing_song = Song.objects.get(slug=song)
                    order_song = OrderSong(
                            order=order,
                            song=existing_song,
                        )
                    order_song.save()
                except Song.DoesNotExist:
                    # displaying error msg, deleting the order and redirecting
                    # to the tracklist
                    messages.error(request, (
                        f'"{song}" was not found in our database.'
                        'Please contact midiDRAGON for assistance.'
                        ))
                    order.delete()
                    return redirect(reverse('tracklist'))

            # redirecting to the order_confirmation page, passing in the order_number
            return redirect(reverse(
                'order_confirmation', args=[order.order_number]
                ))
        else:
            print('the order form is NOT valid')
            # error message that the form isnt valid (they're redirected at
            # the view bottom)
            messages.error(request, (
                'There was an error processing your order form. \n Please ensure all your details have been correctly filled out.'
            ))


class OrderConfirmation(View):
    """
    Class based view inheriting Django's View
    view to handle successful checkouts
    -takes in the request an the order_number for the order just created
    -gets the order by its number
    -displays success msg with the order number
    -delete the bag fro mthe session
    -set template and context
    -return render
    FINISH ...
    """
    def get(self, request, *args, **kwargs):
        """
        FINISH ...
        """

        # getting the order instance from the order number
        order = get_object_or_404(Order, order_number=self.kwargs['order_number'])

        # checking if the user is authenticated before ataching the users profile to the order [when profile app created]
        # if request.user.is_authenticated:
        #     profile = UserProfile.objects.get(user=request.user)
        #     order.user_profile = profile
        #     order.save()

        messages.success(request, f'Your order was successful placed! \n Order number: {order.order_number}. \n A confirmation email will be sent to {order.email}')

        # clearing the session tracklist
        if 'tracklist' in request.session:
            del request.session['tracklist']


        context = {
            'order': order,
        }

        return render(request, 'checkout/order_confirmation.html', context)
