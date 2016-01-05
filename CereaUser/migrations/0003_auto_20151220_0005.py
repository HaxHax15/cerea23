# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaUser', '0002_auto_20151219_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_clinic',
            new_name='is_other',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_owner',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, db_index=True, max_length=255, verbose_name='e-mail'),
        ),
    ]
