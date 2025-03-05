from django.shortcuts import render
from rest_framework import viewsets
from .models import Vaccination
from .serializers import VaccinationSerializer


# Create your views here.
# Vaccination Views
# ViewSet for Vaccination
class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
