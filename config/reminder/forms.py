from django import forms
from .models import *

class RemindersForm(forms.ModelForm):
    date_com = forms.DateTimeField(input_formats=('%Y/%m/%d %I:%M %p', ), widget=forms.DateTimeInput(attrs={'class': 'datetime'}))
    class Meta:
        model = Reminders
        fields = ['title', 'description', 'date_com']

        widgets = {
            'title' : forms.Textarea(attrs={'class' : 'materialize-textarea'}),
            'description' : forms.Textarea(attrs={'class' : 'materialize-textarea'}),
        }