""" models.py for songs app """
import random
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.shortcuts import reverse


class Genre(models.Model):
    """
    Inherits Django's models.Model and represents the Genre table in the
    database
    Only the Admin can create/edit Genres (the unique constraint helps prevent
    duplication)
    Contains the fields:
    name - required and must be unique (programatic name)
    display_name - required and must be unique (name displayed to the user)
    """
    name = models.CharField(max_length=260, unique=True)
    display_name = models.CharField(max_length=260, unique=True)

    class Meta:
        """ meta data for how to order genres """
        ordering = ['name']

    def __str__(self):
        return self.display_name


class Instrument(models.Model):
    """
    Inherits Django's models.Model and represents the Instrument table in the
    database
    Only the Admin can create/edit Instruments (the unique constraint helps
    prevent duplication)
    Contains the fields:
    name - required and must be unique (programatic name)
    display_name - required and must be unique (name displayed to the user)
    """
    name = models.CharField(max_length=260, unique=True)
    display_name = models.CharField(max_length=260, unique=True)

    class Meta:
        """ meta data for how to order instruments """
        ordering = ['name']

    def __str__(self):
        return self.display_name


class ProjectType(models.Model):
    """
    Inherits Django's models.Model and represents the ProjectType table in the
    database
    Only the Admin can create/edit Project Types (the unique constraint helps
    prevent duplication)
    Contains the fields:
    name - required and must be unique (programatic name)
    song_length_range - length range that each projeect type can be (just for
    displaying to the user)
    num_included_instruments - the number of instruments which are included
    with each Project Type (used for setting up the Custom Song form for the
    user)
    num_included_reviews - the number of review sessions which are included
    with each Project Type (used for setting up the Custom Song form for the
    user)
    min_price - the price of each Project Type without any additional
    Instruments/Reviews etc...
    """
    name = models.CharField(max_length=260, unique=True)
    song_length_range = models.CharField(max_length=100)
    num_included_instruments = models.PositiveIntegerField()
    num_included_reviews = models.PositiveIntegerField()
    min_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        """ meta data for how to order project types (cheapest first) """
        ordering = ['min_price']

    def __str__(self):
        return self.name


class Song(models.Model):
    """
    Inherits Django's models.Model and represents the Song table in the
    database
    Contains the fields:
    name - required field but doesnt have to be unique
    image - if not provided a placeholder is used instead
    audio_file - the audio file for the song (downloadable and playable on
    the site)
    video_file - any associated video file (used for if the song is being
    used as a Testimonial and the user wants the video the song was used
    in to be avaliable to view on the site)
    slug - unique identifier for each song to be used in the urls to
    protect the song id's being visible to users
    (set by the unique_slug_generator method if the song doesnt have one -
    the admin can edit the slug but the unique constraint prevents
    accidental duplication)
    project_type - FK to ProjectType model (set to null if the Project Type
    is deleted)
    user - FK to Django's User model (set to null if the user is deleted)
    genre - FK to Genre model (set to null if the Genre is deleted)
    # audio_clip - WOULD HAVE
    bpm - the beats per minute for the song (must be positive and has a
    minimum constraint of 35bpm and maximum of 155bpm)
    duration - the length of the song in minutes and seconds
    price - the price of the song in GBP to 2 d.p. (if I'm not the 'user'
    then the song is a custom song and its price needs to be calculated
    with a pre_save signal every time its updated to override any
    existing value)
    likes - ManyToMany field with Django's User model to keep track of
    the user's who have liked the song
    instruments - ManyToMany field with the Instrument model to store
    the instruments used in the song
    song_purpose - TextField for the user to provide the song's purpose
    (part 1 of the song's details description)
    song_feel - TextField for the user to provide the feel of the song
    (part 2 of the song's details description)
    additional_details - TextField for the user to provide any
    additional details about the song (part 3 of the song's details
    description)
    # song_end_fade - WOULD HAVE
    use_as_testinomial - BooleanField for if the user would like their
    custom song to be used as a Testimonial (False by default)
    testimonial_text - TextField for if the user would like to provide a
    review as part of their song's Testimonial
    completed - BooleanField for if the song is complete (False by default)
    public - BooleanField for if the song can be public (pre-made songs
    will only be visible to users if this is True and custom songs will
    only be visible on the testimonial page if this it True - False by default)
    created_date - DateTimeField set to the current time when the
    song was created (for controlling the ordering of songs displayed)
    Contains the methods:
    number_of_likes - for returning the number of likes
    """
    name = models.CharField(max_length=60)
    image = models.ImageField(blank=True)
    audio_file = models.FileField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    project_type = models.ForeignKey(
        ProjectType,
        null=True,
        on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        User, null=True,
        on_delete=models.SET_NULL,
        related_name='site_user'
    )
    genre = models.ForeignKey(
        Genre,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    bpm = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(35),
            MaxValueValidator(155)
        ]
    )
    duration = models.DurationField(null=True, blank=True)
    price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=6,
        decimal_places=2
    )
    likes = models.ManyToManyField(User, blank=True, related_name='song_like')
    num_of_reviews = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        default='N/A'
    )
    song_purpose = models.TextField(null=True, blank=True)
    song_feel = models.TextField(null=True, blank=True)
    additional_details = models.TextField(null=True, blank=True)
    use_as_testimonial = models.BooleanField(default=False)
    testimonial_text = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ meta data for how to order songs """
        ordering = ['-created_date']

    def number_of_likes(self):
        """ method for counting the number of likes a song has """
        return self.likes.count()

    # ---------- functions for creating the slug on song creation

    def unique_slug_generator(self):
        """
        Method for generating a random slug for each Song instance upon saving
        it.
        This method:
        -generates a list of 20 random integers in the range 0 to 100
        -turns the integer list into a string list
        -joins all the string list items into one string
        -slugifies the song's name
        -combines the random string with the slugified name to get the
        random_slug (to further reduce chances of creating an existing slug)
        -returns the random_slug
        """
        random_numbers_list = [random.randint(0, 100) for i in range(10)]
        random_str_list = [str(i) for i in random_numbers_list]
        random_str = str("".join(random_str_list))
        name_slug = str(slugify(self.name))
        random_slug = name_slug + '-' + random_str

        return random_slug

    def save(self, *agrs, **kwargs):
        """
        Overrides save method
        Sets slug if it doesnt already have one OR if the song name has
        been changed.
        (The change in the song name is checked by splitting the existing slug
        and indexing it so that the number on the end is removed and comparing
        it with the song's name split by spaces, if these don't match, then the
        name has been updated and so the slug is recreated).
        If no audio_file is present, it forces the public
        status to be False so that the song can't be displayed to users.
        (For custom songs, the song doesn't need to be public for the user
        of that song or the admin to view/edit its details)
        Calls the save method again.
        -FINISH
        """

        if not self.slug or not self.slug.split('-')[:-1] == self.name.lower().split(' '):
            print('setting the slug')
            self.slug = self.unique_slug_generator()
            print('slug = ', self.slug)

        if not self.audio_file:
            self.public = False

        if not self.image:
            self.image = 'placeholder.jpg'
        super().save(*agrs, **kwargs)

    def get_absolute_url(self):
        """ method for returning the reverse of the song's absolute url """
        return reverse('song_details', kwargs={'slug': self.slug})

    def __str__(self):
        """ method to return the song name as a string for each song """
        return str(self.name)

    # method for overriding the price with a caluclation IF the song
    # is a custom song (project_type.min_price + every time its updated)


class SongInstrument(models.Model):
    """
    Inherits Django's models.Model and represents the SongInstrument table
    in the database
    Used for associating instruments with a particular song and allowing for
    the song to have multiple of an instrument (e.g. 3 pianos => 3 different
    piano tracks in the song)
    Contains the fields:
    instrument - foriegn key to the instrument model
    song - foriegn key to the song model
    quantity - positive integer representing the number of each instrument in
    the song (e.g. for if there are 3 Electric Guitar tracks in the song)
    """
    instrument = models.ForeignKey(
        Instrument,
        on_delete=models.SET_NULL,
        related_name="instruments_song",
        null=True,
        blank=True
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="song_instruments",
        null=True
    )
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return f'song_instrument_{self.instrument}'
