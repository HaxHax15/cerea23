# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaAnimals', '0005_auto_20160105_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animal_breed',
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_type',
            field=models.ForeignKey(default='', to='CereaAnimals.AnimalType', verbose_name='Тип животного', related_name='+'),
        ),
    ]
