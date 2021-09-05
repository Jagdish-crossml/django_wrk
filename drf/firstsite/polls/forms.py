from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
	"""
	Form for uploading docs and name
	"""
	class Meta:
		model = Document
		fields = ['name','PDF']
class SearchForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name']