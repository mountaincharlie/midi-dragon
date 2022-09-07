""" signals.py file in the songs app for the custom_song_pricec_calculation """
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SongInstrument, Song


# post_save signal for Song model price field when SongInstrument is saved
@receiver(post_save, sender=SongInstrument)
def custom_song_price_calculation(sender, instance, **kwargs):
    """
    Gets the song from the SongInstrument instance
    If the song is not a pre-made song, gets the song's
    project type's; price, number of included reviews
    and number of includeed instruments.
    Gets the number of reviews and instruments that the
    custom song has
    Gets all_song_instrument_objects.
    Calcualtes the number of extra reviews and
    instruments the user has selected.
    If the extra numbers are greater than 0 then the
    extra price is calculated, else they're set to 0
    (since users can have less instruments if they
    want)
    """
    instance_song = instance.song.pk
    song = Song.objects.get(pk=instance_song)

    if not song.user.is_superuser:

        project_type = song.project_type
        project_type_price = project_type.min_price
        project_type_num_included_reviews = project_type.num_included_reviews
        project_type_num_included_instruments = project_type.num_included_instruments

        num_of_reviews = song.num_of_reviews

        all_song_instrument_objects = SongInstrument.objects.all()
        num_of_instruments = 0
        for song_instrument in all_song_instrument_objects:
            if song_instrument.song == song:
                quantity = int(song_instrument.quantity)
                num_of_instruments += 1 * quantity

        num_extra_reviews = int(num_of_reviews) - int(project_type_num_included_reviews)
        num_extra_instruments = int(num_of_instruments) - int(project_type_num_included_instruments)

        if num_extra_reviews > 0:
            extra_reviews_price = int(num_extra_reviews) * settings.ADDITIONAL_REVIEW_SESSION_PRICE
        else:
            extra_reviews_price = 0

        if num_extra_instruments > 0:
            extra_instruments_price = int(num_extra_instruments) * settings.ADDITIONAL_INSTRUMENT_PRICE
        else:
            extra_instruments_price = 0

        custom_song_price = float(project_type_price) + float(extra_instruments_price) + float(extra_reviews_price)

        song.price = custom_song_price
        song.save()
