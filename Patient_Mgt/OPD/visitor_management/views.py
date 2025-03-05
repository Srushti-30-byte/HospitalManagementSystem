from django.shortcuts import render
from rest_framework import viewsets
from .models import VisitorDetails, VisitorList, VisitorPass
from .serializers import (
    VisitorDetailsSerializer,
    VisitorListSerializer,
    VisitorPassSerializer,
)


# Create your views here.
# Visitor Details Views
# ViewSet for Visitor Details
class VisitorDetailsViewSet(viewsets.ModelViewSet):
    queryset = VisitorDetails.objects.all()
    serializer_class = VisitorDetailsSerializer


# Visitor List Views
# ViewSet for Visitor List
class VisitorListViewSet(viewsets.ModelViewSet):
    queryset = VisitorList.objects.all()
    serializer_class = VisitorListSerializer


# Visitor Pass Views
# ViewSet for Visitor Pass
class VisitorPassViewSet(viewsets.ModelViewSet):
    queryset = VisitorPass.objects.all()
    serializer_class = VisitorPassSerializer
