# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaUser', '0004_auto_20151220_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
    ]
