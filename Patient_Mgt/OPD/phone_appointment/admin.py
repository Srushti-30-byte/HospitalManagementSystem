from django.contrib import admin
from .models import PhoneAppointment, PhoneAppointmentList

# Register your models
admin.site.register(PhoneAppointment)
admin.site.register(PhoneAppointmentList)
