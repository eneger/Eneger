from django import forms
from Home import models

class PictureForm(forms.ModelForm):
    class Meta:
        model=models.Picture
        fields=('imagen',)
