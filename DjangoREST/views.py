from django.shortcuts import render
from .models import Hero, City
from .serializers import HeroSerializer, CitySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'population']


    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CitySingle(APIView):
    def get_object(self, id):
        try:
            return City.objects.get(id=id)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, id):
        city = self.get_object(id)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, id):
        city = self.get_object(id)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        city = self.get_object(id)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['gender', 'city_id']
    ordering_fields = ['id', 'name', 'alias']

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HeroSingle(APIView):
    def get_object(self, id):
        try:
            return Hero.objects.get(id=id)
        except Hero.DoesNotExist:
            raise Http404

    def get(self, request, id):
        hero = self.get_object(id)
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    def put(self, request, id):
        hero = self.get_object(id)
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        hero = self.get_object(id)
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




