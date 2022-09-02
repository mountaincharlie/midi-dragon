from django.contrib import admin
from .models import Order, OrderSong


class OrderSongInline(admin.TabularInline):
    """ Tabular inline of the OrderSong table """
    model = OrderSong


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    """

    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'original_tracklist',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'user_profile',
        'full_name',
        'order_total',
        'date',
    )

    ordering = ('-date',)

    search_fields = (
        'order_number',
        'user_profile',
        'full_name',
        'date',
    )

    list_filter = (
        'user_profile',
        'full_name',
        'email',
        'date',
    )

    inlines = [OrderSongInline, ]
