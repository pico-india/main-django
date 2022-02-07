from typing import AbstractSet
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import close_old_connections, models
from django.forms import fields, widgets
from django.forms.fields import EmailField
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
       
    
class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":5}))
    class Meta:
        model = Profile
        fields = ['pf_pic', 'bio', 'insta', 'fb']
        
    