from django.contrib import admin
from .models import Genre, Instrument, ProjectType, Song


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

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

    # actions = any methods you want to define below


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):

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

    # actions = any methods you want to define below


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'song_length_range',
        'num_included_instruments',
        'num_included_reviews',
        'min_price',
    )

    # ordering = ('pk',)

    search_fields = (
        'name',
        'song_length_range',
        'num_included_instruments',
        'num_included_reviews',
        'min_price',
    )

    # list_filter = (
    #     'category',
    #     'price',
    #     'rating',
    # )

    # actions = any methods you want to define below


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):

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
        # dont keep the below
        'image',
        'audio_file',
        'slug',
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
        'instruments',
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
        'instruments',
        'bpm',
        'created_date',
        # 'duration',
        # 'price',
        # 'likes',
    )

    actions = ['change_public_status', 'change_completed_status', 'change_testimonial_status']

    def change_public_status(self, request, queryset):
        """
        Changes the public status of selected songs
        Also checks if the completed status is True before it
        allows the public status to be changed to True (this
        prevents in-completed songs being able to be made public)
        """
        for song in queryset:
            if song.public:
                song.public = False
                song.save()
            elif song.completed and song.audio_file:
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
