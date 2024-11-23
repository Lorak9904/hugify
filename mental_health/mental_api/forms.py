
from django import forms
from .models import MoodLog
from django import forms

class EmotionForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        label="Enter your text"
    )

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood']