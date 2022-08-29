import stripe
from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Order
from .forms import OrderForm
from django.conf import settings
from tracklist.contexts import tracklist_contents


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
            # messages.error(request, 'There are currently no items in your tracklist')
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

        # just a message for if you have to set the var every time
        # if not stripe_public_key:
        #     messages.warning(request, 'Stripe public key is missing. Did you set it in your enviroment?')

        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)
