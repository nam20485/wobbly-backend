from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from api import forms
from api import models

class WobblyUserAdmin(UserAdmin):
    add_form = forms.WobblyUserCreationForm
    form = forms.WobblyUserChangeForm
    model = models.WobblyUser
    list_display = ['email', 'username',]

admin.site.register(models.WobblyUser, WobblyUserAdmin)
admin.site.register(models.WobblyGroup)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Keyword)
