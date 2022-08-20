"""
Django's forms.py for creating the forms I use in views.py
"""

from django import forms
from .models import Song, Instrument, ProjectType, Genre


class DesignCustomSongForm(forms.ModelForm):
    """
    Creating the design custom song form from Django's
    forms.ModelForm
    Sets project_type and genre as ChoiceFields.
    Excluding the song fields:
    -'audio_file' (added by me later)
    -'video_file' (only relevant if the user wants their testimonial to
    include their own video with the song)
    -'slug' (auto generated/updated in save override method)
    -'user' (auto assigned as the creator of the form)
    -'duration' (added by me later)
    -'price' (calculated by JS for on screen and calculated properly in
    the backend for the database saved value)
    -'likes' (n/a until complete and public as testimonial)
    -'completed' (updated by me when complete)
    -'public' (private by default, only public if they allow it as a
    testimonial and its complete and i allow it to be)
    -'created_date' (automatically set on creation)
    """
    project_type = forms.ModelChoiceField(
        label="Project Type", required=True, queryset=ProjectType.objects.all(), empty_label="Select a project type"
    )
    # CHECK THAT WORKS CORRECTLY USING VALUE LIST
    genre = forms.ModelChoiceField(
        label="Song Genre", required=True, queryset=Genre.objects.values_list('display_name', flat=True), empty_label="Select a genre"
    )
    instruments = forms.ModelChoiceField(
        label="Instruments", required=True, queryset=Instrument.objects.values_list('display_name', flat=True), empty_label="Select an instrument"
    )
    num_of_reviews = forms.CharField(label="Number of Review Sessions:")

    class Meta:
        """ meta data for DesignCustomSongForm """
        model = Song
        exclude = (
            'audio_file',
            'video_file',
            'slug',
            'user',
            'duration',
            'price',
            'likes',
            'completed',
            'public',
            'created_date',
        )

        # adding placeholder text with django widgets
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Song Name'}),
            'testimonial_text': forms.Textarea(attrs={'placeholder': 'Write your testimonial review text here [feel free to add a link to your content creation platforms e.g. YouTube channel etc]'}),
            'song_purpose': forms.Textarea(attrs={'placeholder': 'e.g. Youtube video intro'}),
            'song_feel': forms.Textarea(attrs={'placeholder': 'e.g. Starts slow with just piano ... builds until 00:45 and then breaks down to just drums for 20s ...'}),
            'additional_details': forms.Textarea(attrs={'placeholder': 'e.g. Reverb effect on the piano when ... [Add as much detail as you want.]'}),
        }

        labels = {
            'bpm': 'Beats Per Minute [35-155]',
            'testimonial_text': 'Testimonial Review',
            'song_purpose': 'Song Purpose',
            'song_feel': 'Song Feel',
            'additional_details': 'Additional Details',
        }

    #  => user will input
    # name (required char field)
    # image (default placeholder)
    # project_type (dropdown - sets the min_num_reviews and min number of instrument dropdowns)
    # genre (dropdown)
    # bpm (min/max value positive integer)
    # instruments (CHECK THAT HAVING MULTIPLE OF EACH INSTRUMENT WORKS - ELSE MAY NEED A SEPERATE COUNTER FIELD)
    # num_of_reviews (JS button to add more to the min_num_reviews set by the project type)
    # song_purpose (optional textarea)
    # song_feel (optional textarea)
    # additional_details (optional textarea)
    # use_as_testimonial (tickbox, defualt unchecked)
    # testimonial_text (optional textarea appears with JS if tickbox checked - note about the use promoting their social account e.g. YouTube channel)

# CREATE inlineformset for instruments
