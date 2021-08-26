from django import forms
from .models import *
from django.forms import ModelForm, fields
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['avg_rating']

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'        