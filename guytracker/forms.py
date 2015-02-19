from django import forms
from guytracker.models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        exclude = ['lilguy', 'timestamp']

