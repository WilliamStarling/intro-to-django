from .models import Visit
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest, page=""):
    #gets the views object, and increments it by one each time the web page is visited, and then passes the value into the html template.
    #Also saves it to the database so it persists across server restarts.
    v = Visit(page=page)
    if request.user.is_authenticated: #if the user is logged in,
        v.username = request.user.username #updated the username of the visit to be the users username isntead of anonymous.
    v.save()

    visitors = Visit.objects.filter(page=page) #get all the visits to this page.

    context ={
        "page": page,
        "visitors": visitors,
        "num_visits": visitors.count() #sum the number of visitors.
    }
    return render(request, "index.html", status=200, context=context)