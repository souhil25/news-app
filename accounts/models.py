from django.contrib.auth.models import AbstractUser #username, pw1, pw2
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.username

