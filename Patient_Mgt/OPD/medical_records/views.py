from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


# Create your views here.
# Medical Records Views
# ViewSet for Medical Records
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
