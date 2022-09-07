"""
Contains a class for handling Stripe's different webhook events

CREDITS
Logic for the StripeWH_Handler adapted for this project, as well as
how to send emails with gmail SMTP service and how to populate the
email from within Django, from CI walkthrough:
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhook_handler.py

, from Code Institute walkthrough:

"""
import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from songs.models import Song
from .models import Order, OrderSong


class StripeWH_Handler:
    """ Handling Stripe webhook events """

    def __init__(self, request):
        """
        Assigns the request as an attribute of the class
        every time a new instance is created
        """
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Sends the user the order confirmation email
        -gets the songs in the order
        -gets the user's email
        -rendering the txt files to strings and passing a dict
        like a context
        """
        order_songs = OrderSong.objects.filter(order=order)
        customer_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )

        context = {
            'order': order,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
            'order_songs': order_songs,
        }
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            context
        )
        # sending the email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,  # from
            [customer_email]  # to
        )

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

    # ------ methods to handle specific events from Stripe

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment_intent.succeeded webhook from Stripe
        -Used each time the user completes the payment process
        and it is successful
        -Gets the intent and extracts the pid (payment intent id) and
        tracklist data from it
        -Stores billing and tracklist_total details
        -If the user is logged in then it gets the User to be updated
        on the Order model otherwise the user is an AnonymousUser and
        appear as null in the order.user_profile field
        -Sets the order_exists variable to False by default until the
        database has been checked
        -Sets the while loop's 'atempts' to 1
        -Credit for the while loop logic is the same as linked in this file's
        docstring
        -Creates some delay by implementing a while loop to search the db
        to see if the order object exists for the successful playment_intent.
        -The order is searched for using the '_iexact' lookup field on
        each of the fields that the Order model requires and giving them
        values from the cached tracklist data.
        -If the order object is not found within a certain amount of time
        (set by calling the time module's sleep method with a value of 1
        second) for 5 attempts then an order object is created from the
        cached data.
        -If the Order object is found at any point, the while loop is broken
        out of and the _send_confirmation_email() method is called with the
        order instance passed into it
        -The success httpresponse is sent to Stripe with status = 200
        -If the object is not found in this time, then it is likely that
        something went wrong with the form submission even though the payment
        was made successfully, so a Try/Except block is set up to try to
        create the order instance and then each OrderSong instance is created
        -A confirmation email is then sent for the created order and a success
        httpresponse is sent to Stripe.
        -If an error occurs, the created order is deleted, if it exists, and
        an error httpresponse is sent to Stripe with status = 500 (causing
        Stripe to automatically try the request again later)
        """

        intent = event.data.object
        pid = intent.id
        tracklist = intent.metadata.tracklist

        billing_details = intent.charges.data[0].billing_details
        tracklist_total = round(intent.charges.data[0].amount / 100, 2)

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = User.objects.get(username=username)
        print('profile:', profile)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                print('getting the order')
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    order_total=tracklist_total,
                    original_tracklist=tracklist,
                    stripe_pid=pid,
                )
                order_exists = True
                print('ORDER EXISTS')
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)

            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                print('CREATING ORDER')
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=billing_details.name,
                    email=billing_details.email,
                    original_tracklist=tracklist,
                    stripe_pid=pid,
                )
                for song in json.loads(tracklist):
                    existing_song = Song.objects.get(slug=song)
                    order_song = OrderSong(
                            order=order,
                            song=existing_song,
                        )
                    order_song.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}', status=500)

        self._send_confirmation_email(order)

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
