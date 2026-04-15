from .models import Visit
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    #gets the views object, and increments it by one each time the web page is visited, and then passes the value into the html template.
    #Also saves it to the database so it persists across server restarts.
    v = Visit.objects.first()
    v.count += 1
    v.save()

    context ={
        "num_visits": v.count
    }
    return render(request, "index.html", status=200, context=context)