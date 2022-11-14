from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', min_length=4, max_length=50, widget=forms.TextInput(attrs={'class' : 'validate'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'validate'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length = 4)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'validate'}),
            'email' : forms.EmailInput(attrs={'class' : 'validate'}),
            'password1' : forms.PasswordInput(attrs={'class' : 'validate'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'validate'})
        }
    
    def clean_email(self):
        new_email = self.cleaned_data['email'].lower()
        
        email_matches = User.objects.filter(email=new_email).count()
        
        if not new_email:
            raise ValidationError('Email field is required')
        
        if email_matches:
            raise ValidationError(f'Account {new_email} already exists')
        
        return new_email