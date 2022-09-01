"""
Contains a class for handling Stripe's different webhook events which we use to ...FINISH

Logic for the StripeWH_Handler adapted for this project, from CI walkthrough - CREDIT - https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhook_handler.py
"""
import json
import time
from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings
from .models import Order, OrderSong
from songs.models import Song
# from profiles.models import UserProfile


class StripeWH_Handler:
    """ Handling Stripe webhooks """

    def __init__(self, request):
        """
        Assigns the request as an attribute of the class
        every time a new instance is created
        """
        self.request = request

    def handle_event(self, event):
        """
        Handles non-specific webhook event sent from Stripe
        Sends us a hhtp response indictating that Stripe's event
        was recieved
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200
        )


    # ------methods to handle specific events from Stripe

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment_intent.succeeded webhook from Stripe
        Used each time the user completes the payment process
        and it is successful
        If the payment suceeds then a while loop is triggered to
        search the db to see if the order object exists for the
        successful playment_intent.
        The order is searched for using the '_iexact' lookup field on
        each of the fields that the Order model requires and giving them
        values from the cached tracklist data.
        If the order object is not found within a certain amount of time
        (set by calling the time module's sleep method with a value of 1
        second) for 5 attempts
        then an order object is created from the cached data.
        """

        print('REQUEST EXISTS?', self.request)

        # getting the intent and extracting the variables we need from it
        intent = event.data.object
        # pid = payment_intent_id
        pid = intent.id
        tracklist = intent.metadata.tracklist
        # tracklist_json = intent.metadata.tracklist_json
        print('TRACKLIST TYPE', type(tracklist))
        print('TRACKLIST LIST', tracklist)

        # stores billing and tracklist_total details
        billing_details = intent.charges.data[0].billing_details
        tracklist_total = round(intent.charges.data[0].amount / 100, 2)

        # update the user profile
        profile = None  # so that it still works for anonymous users
        username = intent.metadata.username

        # checking if the user is authenticated (can use request.user.is_authenticated aswell)
        # if username != 'AnonymousUser':
            # profile = UserProfile.objects.get(user__username=username)

        # ---- checking if the order already exists (was successful)
        order_exists = False  # set to False by default until found
        attempt = 1
        # creates a bit of delay using a number of while loop iterations to allow time for the payment to be processed before treating it as failed (CREDIT for CI walkthrough in doctsring)
        while attempt <= 5:
            try:
                print('getting the order')
                # finding the order
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    order_total=tracklist_total,
                    original_tracklist=tracklist,
                    stripe_pid=pid,
                )
                order_exists = True
                # breaking from the loop if found
                break
            # if the order hasnt been found yet/doesnt exist
            except Order.DoesNotExist:
                # incrementing attempts if not found yet
                attempt += 1
                time.sleep(1)

        if order_exists:
            print('ORDER EXISTS')  # REMOVE when done
            # send confirmation email
            print('SENDING CONFIRMATION EMAIL...')  # REMOVE when done
            # self._send_confirmation_email(order)
            # http response
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                print('CREATING ORDER')
                # creating the order
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    # order_total=tracklist_total,
                    original_tracklist=tracklist,
                    stripe_pid=pid,
                )
                for song in json.loads(tracklist):
                    # trying to get the song object from its slug (checking it still exists)
                    print('TRACKLIST:', tracklist)
                    print('SONG:', song)
                    existing_song = Song.objects.get(slug=song)
                    print('EXISTING SONG:', existing_song)
                    order_song = OrderSong(
                            order=order,
                            song=existing_song,
                        )
                    order_song.save()
                    # CLEAR SESSION DATA?

            except Exception as e:
                # if anything goes wrong, we need to delete order if it exists
                if order:
                    order.delete()
                # status 500 response casues Stripe to automatically try again later
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}', status=500)

        # send confirmation email
        print('SENDING CONFIRMATION EMAIL....')
        # self._send_confirmation_email(order)

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles payment_intent.payment_failed webhook from Stripe
        Used each time the user completes the payment process
        unsuccessfully
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
