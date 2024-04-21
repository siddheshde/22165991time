from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BirthdateForm(forms.Form):
    birthdate = forms.DateField(label='Enter your birthdate (YYYY-MM-DD)', widget=forms.DateInput(attrs={'type': 'date'}))

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
