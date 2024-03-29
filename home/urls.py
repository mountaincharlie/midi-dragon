""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='home'
    ),
    path(
        'frequently-asked-questions/',
        views.faqs,
        name='faqs'
    ),
    path(
        'terms-of-service/',
        views.tos,
        name='tos'
    ),
    path(
        'privacy-policy/',
        views.privacy,
        name='privacy'
    ),
]
