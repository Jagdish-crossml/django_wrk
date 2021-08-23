from django import forms
from django.forms import ModelForm

from .models import *
   

class ExpenseForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new expense...'}))

	class Meta:
		model = Expense
		fields = '__all__'


TRAVEL='tr'
EDUCATION='ed'
CATEGORIES = [(TRAVEL,'Travel'),(EDUCATION,'education')]

class ChoiceField(forms.ModelForm):
	  choice = forms.ChoiceField(choices = CATEGORIES) 		
