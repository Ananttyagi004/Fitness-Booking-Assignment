from django.contrib import admin
from .models import FitnessClass, Booking


@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'instructor', 'total_slots', 'available_slots')
    search_fields = ('name', 'instructor')
    list_filter = ('date_time', 'instructor')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('fitness_class', 'client_name', 'client_email')
    search_fields = ('client_name', 'client_email')
    list_filter = ('fitness_class',)

