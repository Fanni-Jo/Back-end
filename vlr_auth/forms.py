from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    class ClientForm(forms.Form):
        phone_number = PhoneNumberField(null=False, blank=False, unique=True) # newly added
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
        labels = {'phone_number': 'Mobile Number',} # newly added