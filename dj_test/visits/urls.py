from django.urls import path
from . import views #since this file is already in vists, we don't need to specify we're importing from 'dj_test.visits'. called a relative import.

#have the apps urls here instead of inside of of the projects main urls.py.

app_name = 'visits' #need to have the appname here.

url_patterns = [
    path('', views.index, name='index'),
]