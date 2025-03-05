from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import OPDBill
from .serializers import OPDBillSerializer


# Create your views here.
# OPDBill Views
# ViewSet for OPDBill
class OPDBillViewSet(viewsets.ModelViewSet):
    queryset = OPDBill.objects.all()
    serializer_class = OPDBillSerializer
