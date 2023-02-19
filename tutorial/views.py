from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def index(request):
    response = render(request, 'tutorial/index.html')
    return response

def py_django_page(request):
    response = render(request, 'tutorial/py_django.html')
    return response

def frontend(request):
    response = render(request, 'tutorial/frontend.html')
    return response

def python(request):
    response = render(request, 'tutorial/py.html')
    return response