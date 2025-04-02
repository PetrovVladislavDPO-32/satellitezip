from django.contrib import admin
from .models import SatellitePart

@admin.register(SatellitePart)
class SatellitePartAdmin(admin.ModelAdmin):
    list_display = ('part_number', 'name', 'manufacturer', 'quantity')
    search_fields = ('part_number', 'name')
# Register your models here.
