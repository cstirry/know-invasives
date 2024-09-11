from django import forms
from .models import Plant

class PlantSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label="Plant Name")
    state = forms.CharField(max_length=100, required=False)