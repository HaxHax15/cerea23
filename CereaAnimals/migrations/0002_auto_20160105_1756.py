# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('CereaAnimals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_owner',
            field=models.ForeignKey(related_name='+', verbose_name='Хозяин', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_registrator',
            field=models.ForeignKey(related_name='+', verbose_name='Клиника регистратор', to=settings.AUTH_USER_MODEL),
        ),
    ]
