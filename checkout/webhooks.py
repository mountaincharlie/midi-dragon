"""
Contains a function which listens for webhooks from Stripe ...FINISH

Logic for the webhook function adapted for this project, from CI walkthrough's adaptations - CREDIT - https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhooks.py

Original logic for handling webhooks from the Stripe docs - CREDIT - https://stripe.com/docs/payments/handling-payment-events#create-webhook
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
    """ Listens for webhooks from Stripe """

    # Setup wh_secret and api key
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # gets the webhook data to verify its signature (sig_header)
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # try to create the event
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # generic exception handler from CI walkthrough CREDIT in docstring
        return HttpResponse(content=e, status=400)


    # ----- event handling logic from CI walkthrough CREDIT in docstring

    # sets up an instance of the webhook handler with the request
    handler = StripeWH_Handler(request)

    # event map dict to map webhook events to the required handler functions from StripeWH_Handler class
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # gets the webhook's type from Stripe
    event_type = event['type']

    # gets the required handler if it exists, else uses the generic one
    event_handler = event_map.get(event_type, handler.handle_event)

    # calls the event handler with the event and returns the response to Stripe
    response = event_handler(event)
    return response
