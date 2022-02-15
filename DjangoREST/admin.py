from django.contrib import admin
from .models import Hero, City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'population')

class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias', 'city', 'gender')

admin.site.register(City, CityAdmin)
admin.site.register(Hero, HeroAdmin)