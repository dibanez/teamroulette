from django import forms
from . import models

class TeamForm(forms.Form):
    name = forms.CharField()

class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = models.Player
