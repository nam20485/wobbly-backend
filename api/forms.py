"""
Custom forms
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WobblyUser

class WobblyUserCreationForm(UserCreationForm):
    """
    Custom form for creating WobblyUser's
    """

    class Meta(UserCreationForm):
        model = WobblyUser
        fields = ('username', 'email')

class WobblyUserChangeForm(UserChangeForm):
    """
    Custom form for changing WobblyUser's
    """

    class Meta:
        model = WobblyUser
        fields = ('username', 'email')
