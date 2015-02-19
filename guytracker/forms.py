from django import forms
from guytracker.models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'story_text', 'found_at_lon', 'found_at_lat', 'dropped_at_lon',
                  'dropped_at_lat', 'picture']

