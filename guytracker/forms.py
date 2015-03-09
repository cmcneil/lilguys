from django import forms
from django.db import models
from guytracker.models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        exclude = ['lilguy', 'timestamp', 'dropped_at_lat', 'dropped_at_lon']
        widgets = {'found_at_lat': forms.HiddenInput(),
                   'found_at_lon': forms.HiddenInput()}
    code = forms.CharField(max_length=6, widget=forms.HiddenInput())

