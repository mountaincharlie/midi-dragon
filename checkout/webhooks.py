"""
Contains a function which listens for webhooks from Stripe

CREDITS
-Logic for the webhook function adapted for this project, from CI
walkthrough's adaptations:
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhooks.py

-Original logic for handling webhooks from the Stripe docs:
https://stripe.com/docs/payments/handling-payment-events#create-webhook
"""

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for webhooks from Stripe.
    -Sets up wh_secret and api key
    -Gets the webhook data to verify its signature (sig_header)
    -Tries to create the Stripe Webhook event with these variables
    -The ValueError exception is for invalid payloads
    -The stripe.error.SignatureVerificationError exception is for
    invalid signiture
    -The final exception is a general exception handler
    -The last half of the functions logic is adapted for this project
    from Code Institute's walkthrough [link in file docstring]
    -Sets up an instance of the webhook handler with the request
    -Creates an event map dict to map webhook events to the required
    handler functions from StripeWH_Handler class
    -Gets the webhook's type from Stripe
    -Gets the required handler if it exists, else uses the generic one
    -Calls the event handler with the event and returns the response
    to Stripe
    """

    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # ----- event handling logic from CI walkthrough CREDIT in docstring

    handler = StripeWH_Handler(request)

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
