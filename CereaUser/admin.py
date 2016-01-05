# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username','name', 'is_admin', 'is_owner', 'is_clinic')
    list_filter = ('is_admin',) 
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'name', 'avatar')}),
        ('Permissions', {'fields': ('is_admin', 'is_owner', 'is_clinic', 'is_moderator')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

