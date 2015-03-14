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
    
    def clean_picture(self):
        """Custom validation for the picture field"""
        image = self.cleaned_data.get('picture', False)
        if image:
            if image._size > 10*1024*1024:
                raise forms.ValidationError("Image file too large ( > 10mb )")
            return image
