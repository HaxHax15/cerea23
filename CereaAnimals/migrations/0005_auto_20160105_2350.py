# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaAnimals', '0004_auto_20160105_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='animal_breed',
            field=models.ForeignKey(to='CereaAnimals.AnimalType', default=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_chip_id',
            field=models.CharField(unique=True, max_length=16, verbose_name='ID чипа'),
        ),
    ]
