from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('python-django', views.py_django_page, name='django_course_page'),
    path('frontend', views.frontend, name='frontend_course_page'),
    path('python', views.python, name='python_course_page'),
]