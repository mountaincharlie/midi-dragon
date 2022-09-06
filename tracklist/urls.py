""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.view_tracklist,
        name='tracklist'
    ),
    path(
        'add/<slug:slug>/',
        views.AddToTracklist.as_view(),
        name='add_to_tracklist'
    ),
    path(
        'remove/<slug:slug>/',
        views.RemoveFromTracklist.as_view(),
        name='remove_from_tracklist'
    ),
]
