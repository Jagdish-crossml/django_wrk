from django.forms import ModelForm
from .models import *
class RatingForm(ModelForm):
   class Meta:
     model = Rating
     exclude = ['votes']