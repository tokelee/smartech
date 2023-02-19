from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def index(request):
    description = "Discover a new level of web development and programming with Smartech's professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    response = render(request, 'tutorial/index.html', {'description':description})
    return response

def py_django_page(request):
    response = render(request, 'tutorial/py_django.html', {'title':'Python Django For Web development'})
    return response

def frontend(request):
    response = render(request, 'tutorial/frontend.html', {'title':'Frontend Web Development'})
    return response

def python(request):
    response = render(request, 'tutorial/py.html', {'title':'Python Programming from scratch'})
    return response