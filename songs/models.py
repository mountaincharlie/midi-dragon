from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    """
    """


class Instrument(models.Model):
    """
    """


class ProjectType(models.Model):
    """
    """

 
class Song(models.Model):
    """
    name - required field but doesnt have to be unique
    image - if not provided a placeholder is used instead
    audio_file - the audio file for the song (downloadable and playable on the site)
    video_file - any associated video file (used for if the song is being used as a Testimonial and the user wants the video the song was used in to be avaliable to view on the site)
    slug - unique identifier for each song to be used in the urls to protect the song id's being visible to users (set by the pre_save method only on song creation - the admin can edit the slug but the unique constraint should prevent duplication)
    project_type - FK to ProjectType model (set to null if the Project Type is deleted)
    user - FK to Django's User model (set to null if the user is deleted)
    genre - FK to Genre model (set to null if the Genre is deleted)
    # audio_clip - WOULD HAVE
    bpm - the beats per minute for the song (must be positive and has a minimum constraint of 35bpm and maximum of 155bpm)
    duration - the length of the song in minutes and seconds
    price - the price of the song in GBP to 2 d.p. (if I'm not the 'user' then the song is a custom song and its price needs to be calculated with a pre_save signal every time its updated)
    likes - ManyToMany field with Django's User model to keep track of the user's who have liked the song
    instruments - ManyToMany field with the Instrument model to store the instruments used in the song
    song_purpose - TextField for the user to provide the song's purpose (part 1 of the song's details description)
    song_feel - TextField for the user to provide the feel of the song (part 2 of the song's details description)
    additional_details - TextField for the user to provide any additional details about the song (part 3 of the song's details description)
    # song_end_fade - WOULD HAVE
    use_as_testinomial - BooleanField for if the user would like their custom song to be used as a Testimonial (False by default)
    testimonial_text - TextField for if the user would like to provide a review as part of their song's Testimonial
    completed - BooleanField for if the song is complete (False by default)
    public - BooleanField for if the song can be public (pre-made songs will only be visible to users if this is True and custom songs will only be visible on the testimonial page if this it True - False by default)
    created_date - DateTimeField set to the current time when the song was created (for controlling the ordering of songs displayed)
    """
    name = models.CharField(max_length=260)  # required
    image = models.ImageField(null=True, blank=True)  # set placeholder image?
    audio_file = models.FileField(null=True, blank=True)
    video_file = models.FileField(null=True, blank=True)
    slug = models.SlugField(max_length=200)  #, unique=True, default=random_slug) USE pre/post save signals to generate
    project_type = models.ForeignKey(ProjectType, null=True, blank=True, on_delete=models.SET_NULL)  # set to null if the project type is deleted
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='site_user')
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL)
    # audio_clip = models.FileField(null=True, blank=True)  # WOULD HAVE - for users to provide their own audio clips
    bpm = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(35), MaxValueValidator(155)])
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # overwritten and calculated in pre/post signal if im not the user
    likes = models.ManyToManyField(User, blank=True, related_name='song_like')
    instruments = models.ManyToManyField(Instrument, blank=True, related_name='song_instrument')
    song_purpose = models.TextField(null=True, blank=True)
    song_feel = models.TextField(null=True, blank=True)
    additional_details = models.TextField(null=True, blank=True)
    # song_end_fade = models.BooleanField(default=True)  # WOULD HAVE - option for it to end on the note or fade to silence
    use_as_testinomial = models.BooleanField(default=False)
    testimonial_text = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        """ meta data for how to order songs """
        ordering = ['-created_date']
 
    def __str__(self):
        """ method to return the song name as a string for each song """
        return str(self.name)
 
    def number_of_likes(self):
        """ method for counting the number of likes a song has """
        return self.likes.count()
 
    # method for creating the slug on song creation only
 
    # method for price caluclation IF the song is a custom song (every time its updated)
 