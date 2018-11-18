"""
Models
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
#from PIL import Image


# Text field length constants
MAX_POST_TITLE_LENGTH = 255
MAX_KEYWORD_NAME_LENGTH = 255
MAX_GROUP_NAME_LENGTH = 255



"""
Custom User implementation
"""
class WobblyUser(AbstractUser):
    """
    password = models.CharField(_('password'), max_length=128)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    username = models.CharField(...)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(...)
    is_active = models.BooleanField(...)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    """
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.email


class WobblyGroup(models.Model):
    """
    Custom (Wobbly)Group for users
    """
    owner = models.ForeignKey(WobblyUser, on_delete=models.CASCADE, related_name='owned_groups', related_query_name='owned_group')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=MAX_GROUP_NAME_LENGTH, primary_key=True)
    users = models.ManyToManyField(WobblyUser, related_name='wobbly_groups', related_query_name='wobbly_group')


class Keyword(models.Model):
    """
    Keyword for Posts
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=MAX_KEYWORD_NAME_LENGTH, primary_key=True)


class Post(models.Model):
    """
    Forum Post
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=MAX_POST_TITLE_LENGTH)
    content = models.TextField()
    image = models.ImageField()
    user = models.ForeignKey(WobblyUser, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    wobbly_group = models.ForeignKey(WobblyGroup, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    keywords = models.ManyToManyField(Keyword, related_name='keywords', related_query_name='keyword')



class Comment(models.Model):
    """
    Post Comment
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(WobblyUser, on_delete=models.CASCADE, related_name="comments", related_query_name='comment')
