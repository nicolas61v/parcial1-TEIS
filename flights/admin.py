from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'tipo', 'precio']
    list_filter = ['tipo']
    search_fields = ['nombre']
    ordering = ['id']
