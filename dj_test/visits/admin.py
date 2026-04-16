from django.contrib import admin
from .models import Visit

# Register your models here.
@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "page", "username", "timestamp"]
    list_filter = ["page", "username", "timestamp"] #the different fields we can specify filters for.
    search_fields = ["page", "username"] #the different fields we can specify search for.
    readonly_fields = ["timestamp"] #b/c it's read only, we have to add timestamp here for it to be displayed in the object.