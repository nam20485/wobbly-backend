# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WobblyUser

class WobblyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = WobblyUser
        fields = ('username', 'email')

class WobblyUserChangeForm(UserChangeForm):

    class Meta:
        model = WobblyUser
        fields = ('username', 'email')