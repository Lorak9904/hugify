from django import forms

class EmotionForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        label="Enter your text"
    )