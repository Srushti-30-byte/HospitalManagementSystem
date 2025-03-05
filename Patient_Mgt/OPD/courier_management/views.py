from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import CourierList, CourierDetails
from .serializers import CourierListSerializer, CourierDetailsSerializer


# Create your views here.
# Courier List Views
# ViewSet for Courier List
class CourierListViewSet(viewsets.ModelViewSet):
    queryset = CourierList.objects.all()
    serializer_class = CourierListSerializer


# Courier Details Views
# ViewSet for Courier Details
class CourierDetailsViewSet(viewsets.ModelViewSet):
    queryset = CourierDetails.objects.all()
    serializer_class = CourierDetailsSerializer
