"""
URL configuration for dj_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView
from . import settings


def hello(request):
    return HttpResponse("<h1>Hello,</h1> <p>World!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'visits/favicon_test.ico')), #added favicon.ico as it's own url so it stops being directed to Visits app.
    path('', include('apps.visits.urls')),
]
