""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongsList.as_view(), name='songs'),
    path('<slug:slug>/', views.SongDetailsView.as_view(), name='song_details'),
]
