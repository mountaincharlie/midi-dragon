""" admin.py for the songs app """
from django.contrib import admin
from .models import Genre, Instrument, ProjectType, Song, SongInstrument


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    GenreAdmin class, inheriting admin.ModelAdmin
    """

    list_display = (
        'display_name',
        'name',
        'pk',
    )

    ordering = ('display_name',)

    search_fields = (
        'name',
        'display_name',
    )


class SongInstrumentInline(admin.TabularInline):
    """ Tabular inline of the SongInstrument table """
    model = SongInstrument


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    """
    InstrumentAdmin class, inheriting admin.ModelAdmin
    """

    list_display = (
        'display_name',
        'name',
        'pk',
    )

    ordering = ('pk',)

    search_fields = (
        'name',
        'display_name',
    )


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    """
    ProjectTypeAdmin class, inheriting admin.ModelAdmin
    """

    list_display = (
        'name',
        'song_length_range',
        'num_included_instruments',
        'num_included_reviews',
        'min_price',
    )

    search_fields = (
        'name',
        'song_length_range',
        'num_included_instruments',
        'num_included_reviews',
        'min_price',
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    SongAdmin class, inheriting admin.ModelAdmin
    """

    list_display = (
        'name',
        'user',
        'price',
        'completed',
        'public',
        'project_type',
        'genre',
        'duration',
        'bpm',
        'use_as_testimonial',
        'created_date',
    )

    ordering = ('-created_date',)

    search_fields = (
        'name',
        'image',
        'audio_file',
        'video_file',
        'slug',
        'project_type',
        'user',
        'genre',
        'bpm',
        'duration',
        'price',
        'likes',
        'song_purpose',
        'song_feel',
        'additional_details',
        'use_as_testimonial',
        'testimonial_text',
        'completed',
        'public',
        'created_date',
    )

    list_filter = (
        'completed',
        'public',
        'use_as_testimonial',
        'project_type',
        'user',
        'genre',
        'bpm',
        'created_date',
    )

    inlines = [SongInstrumentInline, ]

    actions = [
        'change_public_status',
        'change_completed_status',
        'change_testimonial_status'
    ]

    def change_public_status(self, request, queryset):
        """
        Changes the public status of selected songs, but only allows
        them to be made public if certain conditions apply.
        Checks first that the song is complete and has an audio file.
        If it does, then it checks if either the song user is a regular
        user (custom song) AND the song has use_as_testimonial = True OR
        that the song's user is the superuser (pre-made songs).
        In either of these cases, the song can be made public.
        This prevents in-complete songs or songs with missing audio files
        from being made public accidetnally as well as making sure that the
        only completed custom songs that can be public are ones that the song
        user has approved to be used as a testimonial.
        """

        for song in queryset:
            if song.public:
                song.public = False
                song.save()
            elif song.completed and song.audio_file:
                if not song.user.is_superuser and song.use_as_testimonial or song.user.is_superuser:
                    song.public = True
                    song.save()

    def change_completed_status(self, request, queryset):
        """
        Changes the completed status of selected songs
        Also sets the public status to False if the completed status
        is being set to False to prevent in-complete songs/songs
        needing work from being visible to users.
        """
        for song in queryset:
            if song.completed:
                song.completed = False
                song.public = False
                song.save()
            else:
                song.completed = True
                song.save()

    def change_testimonial_status(self, request, queryset):
        """
        Changes the testimonial status of selected songs
        Doesn't need to check that the song is completed since
        in-complete custom songs can have the 'Use As Testimonial'
        option selected - they just won't be visible on the
        Testimonial page until the song is public (which requires
        it to be complete)
        """
        for song in queryset:
            if song.use_as_testimonial:
                song.use_as_testimonial = False
                song.save()
            else:
                song.use_as_testimonial = True
                song.save()
