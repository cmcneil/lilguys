from django import forms
from django.db import models
from guytracker.models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        exclude = ['lilguy', 'timestamp', 'dropped_at_lat', 'dropped_at_lon']
    code = forms.CharField(max_length=6, widget=forms.HiddenInput())

