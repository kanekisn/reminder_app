from django import forms
from .models import *
from django.core.exceptions import ValidationError
import datetime
import pytz

class RemindersForm(forms.ModelForm):
    date_com = forms.DateTimeField(input_formats=('%Y/%m/%d %I:%M %p', ), widget=forms.DateTimeInput(attrs={'class': 'datetime'}))
    class Meta:
        model = Reminders
        fields = ['title', 'description', 'date_com']

        widgets = {
            'title' : forms.Textarea(attrs={'class' : 'materialize-textarea'}),
            'description' : forms.Textarea(attrs={'class' : 'materialize-textarea'}),
        }
    
    def clean_date_com(self):
        new_date = self.cleaned_data['date_com']
        
        if new_date < datetime.datetime.utcnow().replace(tzinfo=pytz.UTC):
            raise ValidationError('Use correct date!')
        
        return new_date
        