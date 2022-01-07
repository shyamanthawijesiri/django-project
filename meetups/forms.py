from django import forms
from django.forms import fields, models

from .models import Participants

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['email']