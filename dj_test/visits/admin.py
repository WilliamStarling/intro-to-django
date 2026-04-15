from django.contrib import admin
from .models import Visit

# Register your models here.
@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    pass