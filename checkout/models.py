import uuid  # for generating the order numbers
from django.db import models
from songs.models import Song

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# BASED ON CI WALKTHROUGH MODEL - ADAPTED FOR THIS PROJECT
class Order(models.Model):
    """
    Representing the entire contents of the user's Tracklist
    when they place their order.
    Contains the fields:
    order_number - non-editable 32 digit string generated using
    python's uuid
    user_profile - TO BE ADDED ON CREATION OF THE PROFILE APP 
    (if the UserProfile instance is deleted, this field will be
    set to Null, so that the order wont be lost)
    full_name - will be an editable input on the checkout page
    populated from a logged in user's profile OR left blank for
    non-logged in users
    email - will be an editable input on the checkout page
    populated from a logged in user's profile OR left blank for
    non-logged in users
    date - auto generated on the creation of the Order instance
    (this is used to order the Orders in the user's Order History)
    order_total - updated for every song in the Order
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)

    # related_name => could call user.user_profile.my_orders
    # user_profile = models.ForeignKey(
    #     UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_orders'
    #     )

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    # THE BELOW MAY BE REQUIRED LATER WHEN SETTING UP STRIPE
    # original_bag = models.TextField(null=False, blank=False, default='')
    # stripe_pid = models.CharField(
    #     max_length=254, null=False, blank=False, default=''
    #     )

    class Meta:
        """ meta data for how to order orders """
        ordering = ['-date']

    def _generate_order_number(self):
        """
        Generates random unique 32 digit order number with uuid
        Prepended with _ to indicate its only used in this class
        Uses python's Universal Unique Identifier module uuid,
        with:
        .uuid4() - to generate a random UUID
        .hex - to make it a 32-character lowercase hexadecimal string
        .upper() - to convert any letters to uppercase (for clarity)
        """
        order_number = uuid.uuid4().hex.upper()

        return order_number

    # communicates with ordersong post_save signal?
    def update_total(self, song_price):
        """
        Updates the total everytime a new song is added to
        or removed from the order by adding the 'song_price'
        passed in from the post_save (as a positive number) or
        post_delete (as a negative number) signals
        Uses the 'orderitems' related_name
        """

        self.order_total += song_price
        self.save()  # saves the instance

    def save(self, *agrs, **kwargs):
        """
        Overrides save method
        Sets order number if it doesnt already have one
        Calls the save method again
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*agrs, **kwargs)

    def __str__(self):
        """ Returns the order_number """
        return self.order_number


class OrderSong(models.Model):
    """
    Represents each song in the order
    Contains the FK fields:
    order - to Order model (if the order instance is deleted, then
    the associated OrderSong instances are deleted, since they aren't
    needed if the Order instance doesnt exist)
    song - to Song model (if the Song instance is deleted, then all
    the associated OrderSong songs are set to null so that these records
    aren't missing on the order since the order will still exist)
    """
    # contains the order date
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='ordersongs'
    )
    # contains the song price for the order total calc
    song = models.ForeignKey(
        Song,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='songs_order'
    )

    def __str__(self):
        """ Returns the song name and order_number it belongs to """
        return f'SKU {self.song.name} on order {self.order.order_number}'


# MOVE SIGNALS INTO A SEPERATE signals.py file

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

    instance.order.update_total(song_price)
