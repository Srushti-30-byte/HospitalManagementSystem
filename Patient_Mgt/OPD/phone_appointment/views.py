from django.shortcuts import render
from rest_framework import viewsets
from .models import PhoneAppointment, PhoneAppointmentList
from .serializers import PhoneAppointmentSerializer, PhoneAppointmentListSerializer


# Create your views here.
# Phone Appointment Views
# ViewSet for PhoneAppointment
class PhoneAppointmentViewSet(viewsets.ModelViewSet):
    queryset = PhoneAppointment.objects.all()
    serializer_class = PhoneAppointmentSerializer


# Create your views here.
# Phone Appointment List Views
# ViewSet for PhoneAppointmentList
class PhoneAppointmentListViewSet(viewsets.ModelViewSet):
    queryset = PhoneAppointmentList.objects.all()
    serializer_class = PhoneAppointmentListSerializer
