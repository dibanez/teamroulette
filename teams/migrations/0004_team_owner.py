# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0003_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=True,
        ),
    ]
