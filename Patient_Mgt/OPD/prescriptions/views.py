from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer


# Create your views here.
# Prescription Views
# ViewSet for Prescriptions
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
