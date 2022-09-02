""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ProfileDashboard.as_view(), name='dashboard'),
]
