from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)
	phone_number = PhoneNumberField(null=False, blank=False, unique=True)
	class Meta:
		model = Profile
		fields = ("first_name","last_name","username", "email","phone_number","password1", "password2","profile_picture")

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


