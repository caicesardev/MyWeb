from django.shortcuts import render
from .models import *


def home(request):
    context = {}
    return render(request, 'portfolio/home.html')


def projects(request):
    context = {}
    return render(request, 'portfolio/projects.html')


def about(request):
    context = {}
    return render(request, 'portfolio/about.html')


def faq(request):
    context = {}
    return render(request, 'portfolio/faq.html')


def blog(request):
    context = {}
    return render(request, 'portfolio/blog.html')


def contact(request):
    context = {}
    return render(request, 'portfolio/contact.html')
