"""
Django's forms.py for creating the forms I use in views.py
"""

from django import forms
from django.contrib.auth.models import User


class MyDetailsForm(forms.ModelForm):
    """
    Creates the profile_dashboard My Details form from Django's
    forms.ModelForm
    """

    class Meta:
        """ meta data for MyDetailsForm """
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

        # adding placeholder text with django widgets
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }
