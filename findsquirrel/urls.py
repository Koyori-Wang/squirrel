from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<str:squirrel_id>/', views.detail, name='detail'),
]
