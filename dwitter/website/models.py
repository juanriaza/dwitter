from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.CharField(blank=True, max_length=200)


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser)

    def __str__(self):
        return self.message
