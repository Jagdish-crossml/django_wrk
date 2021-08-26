from django.forms import forms
from django.forms import ModelForm
from .models import *
class ProjectSettings(forms.Form):
    artists = forms.CharField(max_length=200)

    def __init__(self, qs=None, *args, **kwargs):
        super(ProjectSettings, self).__init__(*args, **kwargs)
        if qs:
            self.fields['artists'] = forms.ModelMultipleChoiceField(queryset=qs, widget=forms.CheckboxSelectMultiple())