"""
Django's forms.py for creating the forms I use in views.py
credit:
https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/
for how to create the inline formset for SongInstrument
"""

from django import forms
from .models import Song, Instrument, ProjectType, Genre, SongInstrument


class DesignCustomSongForm(forms.ModelForm):
    """
    Creates the design custom song form from Django's
    forms.ModelForm
    Sets project_type and genre as ChoiceFields with values for
    'empty_label'
    Excludes the song fields:
    -'audio_file' (added by me later)
    -'video_file' (only relevant if the user wants their testimonial to
    include their own video with the song)
    -'slug' (auto generated/updated in save override method)
    -'user' (auto assigned as the creator of the form in the view post method)
    -'duration' (added by me later)
    -'price' (calculated by JS for on screen and calculated properly in
    the backend for the database saved value)
    -'likes' (n/a until complete and public as testimonial)
    -'completed' (updated by me when complete)
    -'public' (private by default, only public if they allow it as a
    testimonial and its complete and i allow it to be)
    -'created_date' (automatically set on creation)
    Uses Django widgets to add placeholders to the textarea and name
    input fields
    Adds labels to fields which don't have them disaplyed
    """
    project_type = forms.ModelChoiceField(
        label="Project Type", required=True, queryset=ProjectType.objects.all(), empty_label="Select a project type"
    )

    genre = forms.ModelChoiceField(
        label="Song Genre", required=True, queryset=Genre.objects.all(), empty_label="Select a genre"
    )

    num_of_reviews = forms.CharField(label="Number of Review Sessions", required=False)

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
            'testimonial_text': forms.Textarea(attrs={'placeholder': 'Write your testimonial review text here ... [feel free to add a link to your content creation platforms e.g. YouTube channel etc]'}),
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


class AddSongInstrumentForm(forms.ModelForm):
    """
    Creates the add SongInstrument form from Django's
    forms.ModelForm
    Excludes the song field from the SongInstrument
    table model
    Sets the instrument field as a ModelChoiceField
    and with an 'empty_label' for when no option is selected
    yet
    """
    class Meta:
        """ meta data for AddSongInstrumentForm """
        model = SongInstrument
        exclude = ('song',)

    instrument = forms.ModelChoiceField(
        label="Instrument", queryset=Instrument.objects.all(), empty_label="Select an instrument"
    )


# using inlineformset_factory to handle the AddSongInstrumentForm
AddSongInstrumentFormSet = forms.inlineformset_factory(
    Song,
    SongInstrument,
    form=AddSongInstrumentForm,
    extra=0
)
