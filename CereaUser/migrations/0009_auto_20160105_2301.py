# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaUser', '0008_auto_20160105_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Админ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_clinic',
            field=models.BooleanField(default=False, verbose_name='Клиника'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_other',
            field=models.BooleanField(default=False, verbose_name='Остальное'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='Хозяин'),
        ),
    ]
