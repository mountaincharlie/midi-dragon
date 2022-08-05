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

    # actions = any methods you want to define below
    # public, completed and use_as_testimonial toggles
