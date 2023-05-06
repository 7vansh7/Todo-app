from django.forms import ModelForm
from django import forms
from .models import Item

class itemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields= '__all__'