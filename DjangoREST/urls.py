from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/cities/', views.CityList.as_view()),
    path('api/cities/<int:id>/', views.CitySingle.as_view()),
    path('api/heroes/', views.HeroList.as_view()),
    path('api/heroes/<int:id>/', views.HeroSingle.as_view()),
]