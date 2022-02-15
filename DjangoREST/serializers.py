from rest_framework import serializers
from .models import Hero, City


class CitySerializer(serializers.ModelSerializer):
   class Meta:
       model = City
       fields = ['id', 'name', 'population']

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
       model = Hero
       fields = ['id', 'name', 'alias', 'city', 'gender']