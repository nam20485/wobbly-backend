from django.db import models
from django.contrib.auth.models import AbstractUser

class WobblyUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email
