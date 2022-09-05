from django.shortcuts import render
from checkout.models import Order, OrderSong


def index(request):
    """
    View for returning the index.html
    If the user has just logged in, it checks if songs which may have been
    added to the tracklist before they logged in, have already been purchased
    by that user, then they are removed from their tracklist so that they
    don't accidentally purchase them twice.
    The check:
    -gets the tracklist songs from the session (or an empty string if it
    doesn't exist yet)
    -gets all of the user's orders
    -creates an empty list to add all of the songs which have been ordered
    by the user
    -for each order, it then gets all of the associated OrderSong objects
    -for each ordersong in order_songs it then appends the ordersong
    by its .song.slug to the songs_ordered_by_user list
    -then for each ordered_song in the songs_ordered_by_user list, if
    that song slug exists in the tracklist list, then it is removed from
    the tracklist list
    """

    if request.user.is_authenticated:

        tracklist = request.session.get('tracklist', [])
        users_orders = Order.objects.filter(user_profile=request.user.id)

        songs_ordered_by_user = []
        for order in users_orders:
            order_songs = OrderSong.objects.filter(order=order)
            for ordersong in order_songs:
                songs_ordered_by_user.append(ordersong.song.slug)

        for ordered_song in songs_ordered_by_user:
            if ordered_song in tracklist:
                tracklist.remove(ordered_song)

    return render(request, 'home/index.html')


def faqs(request):
    """
    View for returning the FAQs.html
    """

    return render(request, 'home/FAQs.html')


def tos(request):
    """
    View for returning the terms_of_service.html
    """

    return render(request, 'home/terms_of_service.html')


def privacy(request):
    """
    View for returning the privacy_policy.html
    """

    return render(request, 'home/privacy_policy.html')
