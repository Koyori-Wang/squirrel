from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel
from .form import SquirrelForm

def index(request):
    return render(request, 'findsquirrel/index.html')

# Create your views here.

