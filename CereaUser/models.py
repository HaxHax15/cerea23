# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
            name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='e-mail',
        max_length=255,
        unique=True,
        db_index=True)
    username = models.CharField(
        verbose_name='Ник',
        max_length=255,
        unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/%Y/%m/%d',
        blank=True,
        null=True)
    name = models.CharField(
        verbose_name='Ф.И.О.',
        max_length=255,
        blank=False,
        null=False)
    date_of_birth = models.DateField(
        verbose_name='День рождения',
        blank=True,
        null=True)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен')
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Админ')
    is_owner = models.BooleanField(
        default=False,
        verbose_name='Хозяин')
    is_moderator = models.BooleanField(
        default=False,
        verbose_name='Модератор')
    is_clinic = models.BooleanField(
        default=False,
        verbose_name='Клиника')
    is_other = models.BooleanField(
        default=False,
        verbose_name='Остальное')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return '%s' % (self.name,)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def isclinic(self):
        return self.is_clinic

    def isowner(self):
        return self.is_owner

    def isother(self):
        return self.is_other

    def ismoderator(self):
        return self.is_moderator

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователь"
