from django.shortcuts import render
from rest_framework import viewsets
from .models import PhoneAppointment
from .serializers import PhoneAppointmentSerializer


# Create your views here.
# Phone Appointment Views
# ViewSet for PhoneAppointment
class PhoneAppointmentViewSet(viewsets.ModelViewSet):
    queryset = PhoneAppointment.objects.all()
    serializer_class = PhoneAppointmentSerializer
