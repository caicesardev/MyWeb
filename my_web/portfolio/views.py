from django.shortcuts import render
from .models import *


def home(request):
    context = {}
    return render(request, 'portfolio/home.html')


def about(request):
    context = {}
    return render(request, 'portfolio/about.html')
