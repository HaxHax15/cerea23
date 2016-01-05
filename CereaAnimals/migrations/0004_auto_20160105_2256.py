# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CereaAnimals', '0003_auto_20160105_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Животное', 'verbose_name_plural': 'Животное'},
        ),
        migrations.AlterModelOptions(
            name='animalbreed',
            options={'verbose_name': 'Порода животного', 'verbose_name_plural': 'Порода животного'},
        ),
        migrations.AlterModelOptions(
            name='animaltype',
            options={'verbose_name': 'Тип животного', 'verbose_name_plural': 'Тип животного'},
        ),
    ]
