""" contains the update_on_save() and update_on_delete() signals """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderSong


@receiver(post_save, sender=OrderSong)
def update_on_save(sender, instance, created, **kwargs):
    """
    Handles functions from the OrderSong models post_save event
    sender => OrderSong
    instance => the instance of the OrderSong that sent it
    created = > django boolean for if this is a new instance or being updated
    Reciver decorator to pass info about whats happening here
    For the instance of OrderSong, it calls the Order model's update_total()
    method, passing in the price of the song.
    """
    song_price = instance.song.price

    print('UPDATE ON SAVE CALLED')

    instance.order.update_total(song_price)


@receiver(post_delete, sender=OrderSong)
def update_on_delete(sender, instance, **kwargs):
    """
    Handles functions from the OrderSong models post_delete event
    sender => OrderSong
    instance => the instance of the OrderSong that sent it
    Reciver decorator to pass info about whats happening here
    For the instance of OrderSong, it calls the Order model's update_total()
    method, passing in the negative of price of the song (so that when its
    added to the order_total in the update_total() method, it will actually
    be subtracting from the total).
    """
    song_price = (instance.song.price) * -1

    print('UPDATE ON DELETE CALLED')

    instance.order.update_total(song_price)
