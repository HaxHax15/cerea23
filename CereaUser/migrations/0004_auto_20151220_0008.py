# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaUser', '0003_auto_20151220_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_clinic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]
