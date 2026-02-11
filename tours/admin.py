from django.contrib import admin
from .models import Destination, TourPackage, Booking, ContactMessage

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(TourPackage) 
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "price", "duration_days", "available_slots")   
    list_filter = ("destination",)
    search_fields = ("title",)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "package", "email", "number_of_people", "booked_at","phone","message")
    list_filter = ("status",)
    search_fields = ("full_name", "phone", "email")
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', "email", "subject", "message")
    list_filter = ("sent_at",)
    search_fields = ('full_name', "email")