from django.shortcuts import render
from django.core.mail import send_mail
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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # send mail
        send_mail(
            subject,  # subject
            message,  # message
            email,  # from email
            ['caicesardev@gmail.com'],  # to email
        )
        return render(request, 'portfolio/contact.html', {'name': name})
    else:
        return render(request, 'portfolio/contact.html')
