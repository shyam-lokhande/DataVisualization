from django import forms

from .models import *

class CsvForm(forms.ModelForm):
    class Meta:
        model=CsvUpload
        fields=('file_name',)