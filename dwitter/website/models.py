from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tweet(models.Model):
    message = models.TextField(blank=True, max_length=140)
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.message
