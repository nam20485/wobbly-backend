"""
admin interface configuration
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api import forms
from api import models

class WobblyUserAdmin(UserAdmin):
    """
    add custom WobblyUser creation form to support our custom user class
    """
    add_form = forms.WobblyUserCreationForm
    form = forms.WobblyUserChangeForm
    model = models.WobblyUser
    list_display = ['email', 'username',]

admin.site.register(models.WobblyUser, WobblyUserAdmin)
admin.site.register(models.WobblyGroup)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Keyword)
