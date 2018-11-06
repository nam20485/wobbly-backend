from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import WobblyUserCreationForm, WobblyUserChangeForm
from .models import WobblyUser

class WobblyUserAdmin(UserAdmin):
    add_form = WobblyUserCreationForm
    form = WobblyUserChangeForm
    model = WobblyUser
    list_display = ['email', 'username',]

admin.site.register(WobblyUser, WobblyUserAdmin)
