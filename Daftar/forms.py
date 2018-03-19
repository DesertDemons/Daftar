from django import forms
from .models import Profile, Post
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'context']

