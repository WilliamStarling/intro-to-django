from django.db import models

# Create your models here.

class Visit(models.Model):
    page = models.CharField(max_length=255) #the page that is being tracked, default is the home page
    username = models.CharField(max_length=255, default="anonymous") #the username of the visitor, default is anonymous
    timestamp = models.DateTimeField(auto_now_add=True) #the timestamp of the visit, automatically set to the current time when the object is created