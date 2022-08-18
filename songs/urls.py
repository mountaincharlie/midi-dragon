""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongsList.as_view(), name='songs'),
    path('<slug:slug>/', views.SongDetailsView.as_view(), name='song_details'),
    path('<slug:slug>/likes', views.LikeSong.as_view(), name='song_like'),
    path('<slug:slug>/download/', views.DownloadSong.as_view(), name='download_song'),
]
