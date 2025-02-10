from django import forms

from la2.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('userEmail', 'server', 'message')
        labels = {
            'userEmail': 'Email',
            'server': 'Server',
            'message': 'Your message'
        }
        widgets = {
            'userEmail': forms.TextInput(attrs={'class': 'feedback__input'}),
            'server': forms.Select(attrs={'class': 'feedback__select'}),
            'message': forms.Textarea(attrs={'class': 'feedback__textarea'}),
        }