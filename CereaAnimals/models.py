from django.db import models
from CereaUser.models import User
from smart_selects.db_fields import ChainedForeignKey


class Animal(models.Model):
    """
    Животное
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    animal_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name='Кличка')
    animal_chip_id = models.CharField(
        max_length=16,
        blank=False,
        unique=True,
        verbose_name='ID чипа')
    animal_sex = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=False,
        verbose_name='Пол животного')
    animal_type = models.ForeignKey('AnimalType',
                                    blank=False,
                                    related_name='+',
                                    verbose_name='Тип животного',
                                    default=''
                                    )

    animal_owner = models.ForeignKey(User,
                                     limit_choices_to={'is_owner': True},
                                     blank=False,
                                     related_name='+',
                                     verbose_name='Хозяин')
    animal_registration_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата регистрации')
    animal_registrator = models.ForeignKey(
        User,
        limit_choices_to={'is_clinic': True},
        blank=False,
        related_name='+',
        verbose_name='Клиника регистратор')

    def __str__(self):
        return self.animal_name+'('+self.animal_chip_id+')'

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животное"


class AnimalType(models.Model):
    """
    Тип животного
    """
    AnimalType_name = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        verbose_name='Тип животного')

    def __str__(self):
        return self.AnimalType_name

    class Meta:
        verbose_name = "Тип животного"
        verbose_name_plural = "Тип животного"


class AnimalBreed(models.Model):
    """
    Порода
    """
    AnimalBreed_name = models.CharField(
        max_length=24,
        blank=False,
        null=False,
        verbose_name='Порода животного')
    AnimalType_id = models.ForeignKey(
        AnimalType,
        null=False,
        blank=False,
        verbose_name='Тип животного')

    def __str__(self):
        return self.AnimalBreed_name

    class Meta:
        verbose_name = 'Порода животного'
        verbose_name_plural = 'Порода животного'

