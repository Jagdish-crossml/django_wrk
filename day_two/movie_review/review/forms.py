from django import forms
from .models import *
from django.forms import ModelForm
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['awards','artists']