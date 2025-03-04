from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import RegularRegistration
from .serializers import RegularRegistrationSerializer


# Create your views here.
# Express Registration Views
# ViewSet for ExpressRegistration
class RegularRegistrationViewSet(viewsets.ModelViewSet):
    queryset = RegularRegistration.objects.all()
    serializer_class = RegularRegistrationSerializer
