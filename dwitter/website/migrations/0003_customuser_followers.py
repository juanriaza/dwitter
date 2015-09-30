# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following', blank=True),
        ),
    ]
