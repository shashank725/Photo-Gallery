from dataclasses import field
from pyexpat import model
from django import forms
from .models import gallery

class galleryForm(forms.ModelForm):
    class Meta:
        model = gallery
        fields = '__all__'