"""
Django's forms.py for creating the form I use in views.py
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Using the Order model and with only the editable non-auto generated fields
    avaliable
    """

    class Meta:
        """ meta form data for OrderForm """
        model = Order
        fields = (
            'full_name',
            'email',
        )

        # adding placeholder text with django widgets
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
        }
