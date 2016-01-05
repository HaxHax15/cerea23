# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaAnimals', '0002_auto_20160105_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_chip_id',
            field=models.CharField(verbose_name='ID чипа', max_length=16),
        ),
    ]
