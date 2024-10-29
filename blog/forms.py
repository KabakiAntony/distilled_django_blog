from django import forms
from .models import Blogs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'content']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

