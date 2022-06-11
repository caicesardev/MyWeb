from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects', views.projects, name="projects"),
    path('about', views.about, name="about"),
    path('preguntas-frecuentes', views.faq, name="faq"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
]
