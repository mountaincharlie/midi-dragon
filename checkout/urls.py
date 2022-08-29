""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
]
