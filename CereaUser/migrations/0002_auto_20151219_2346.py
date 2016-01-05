# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
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
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ф.И.О.', blank=True),
        ),
    ]
