from django import forms
from django.forms import ModelForm

from .models import *


class ExpenseForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Add new expense...'}))


    # comment = forms.CharField(widget=forms.TextInput(
    #      attrs={'placeholder': 'Add new comment...'}))


    class Meta:
      model = Expense
      fields = '__all__'
