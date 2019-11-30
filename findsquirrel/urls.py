from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/<str:squirrel_id>/', views.detail, name='detail'),
]
