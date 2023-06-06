from django.contrib import admin
from .models import Department
from .models import Doctors, Booking
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
# admin.site.register(Job)
admin.site.register(Booking)

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')
# admin.site.register(Booking, BookingAdmin)

