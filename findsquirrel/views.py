from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel
from .form import SquirrelForm

def index(request):
    return render(request, 'findsquirrel/index.html')

def map(request):
    latlong = list()
    for i in Squirrel.objects.all():
        l_dict = {}
        l_dict['latitude']=i.latitude
        l_dict['longitude']=i.longitude
        latlong.append(l_dict)
    return render(request, 'findsquirrel/map.html', {'latlong':latlong})

def sightings(request):
    squirrel_id = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'findsquirrel/sightings.html', {'squirrel_id':squirrel_id})

# Create your views here.

