# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('animal_name', models.CharField(verbose_name='Кличка', max_length=64)),
                ('animal_chip_id', models.IntegerField(verbose_name='ID чипа')),
                ('animal_sex', models.CharField(verbose_name='Пол животного', choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('animal_registration_date', models.DateTimeField(verbose_name='Дата регистрации', auto_now=True)),
                ('animal_owner', models.ForeignKey(verbose_name='Хозяин', to=settings.AUTH_USER_MODEL, related_name='owner')),
                ('animal_registrator', models.ForeignKey(verbose_name='Клиника регистратор', to=settings.AUTH_USER_MODEL, related_name='clinic')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('AnimalBreed_name', models.CharField(verbose_name='Порода животного', max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('AnimalType_name', models.CharField(verbose_name='Тип животного', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='animalbreed',
            name='AnimalType_id',
            field=models.ForeignKey(verbose_name='Тип животного', to='CereaAnimals.AnimalType'),
        ),
    ]
