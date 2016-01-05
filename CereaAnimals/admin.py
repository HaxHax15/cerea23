from django.contrib import admin
from .models import Animal, AnimalBreed, AnimalType

admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(AnimalBreed)
