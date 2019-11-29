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
    latlong = latlong[:20]
    return render(request, 'findsquirrel/map.html', {'latlong':latlong})

def sightings(request):
    squirrel_id = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'findsquirrel/sightings.html', {'squirrel_id':squirrel_id})

def detail(request, squirrel_id):
    data = Squirrel.objects.get(squirrel_id=squirrel_id)
    if request.method == "POST":
        if 'delete' in request.POST:
            data.delete()
        else:
            data = SquirrelForm(instance=data,data=request.POST)
            data.save()
        return redirect('/findsquirrel/sightings/')
    return render(request, 'findsquirrel/detail.html', {'data':data})

def add(request):
    if request.method == "POST":
        new_squirrel = SquirrelForm(request.POST)
        new_squirrel.save()
        return redirect('/findsquirrel/sightings/')
    return render(request, 'findsquirrel/add.html')

def stats(request):
    dataset = Squirrel.objects \
        .values('shift') \
        .annotate(running_count=Count('shift', filter=Q(running=True)),
                not_running_count=Count('shift', filter=Q(running=False)),
                chasing_count=Count('shift', filter=Q(chasing=True)),
                not_chasing_count=Count('shift', filter=Q(chasing=False)),
                climbing_count=Count('shift', filter=Q(climbing=True)),
                not_climbing_count=Count('shift', filter=Q(climbing=False)),
                eating_count=Count('shift', filter=Q(eating=True)),
                not_eating_count=Count('shift', filter=Q(eating=False)),
                foraging_count=Count('shift', filter=Q(foraging=True)),
                not_foraging_count=Count('shift', filter=Q(foraging=False))) \
        .order_by('shift')
    return render(request, 'findsquirrel/stats.html', {'dataset': dataset})

# Create your views here.

