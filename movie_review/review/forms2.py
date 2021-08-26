from django.forms import ModelForm
from .models import *
class SearchForm(ModelForm):
   class Meta:
     model = Movie
     fields = [ 'name']