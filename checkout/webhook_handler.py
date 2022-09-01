"""
Contains a class for handling Stripe's webhooks which we use to ...FINISH

Logic for the StripeWH_Handler adapted for this project, from CI walkthrough - CREDIT - https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhook_handler.py
"""
from django.http import HttpResponse


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
