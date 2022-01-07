from django import forms
from django.forms import fields, models

from .models import Participants

# class RegistrationForm(forms.ModelForm):
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='your email')
    # class Meta:
    #     model = Participants
    #     fields = ['email']