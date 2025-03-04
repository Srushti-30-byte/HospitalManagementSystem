from django.shortcuts import render
from rest_framework import viewsets
from .models import ExpressRegistration
from .serializers import ExpressRegistrationSerializer


# Create your views here.
# Express Registration Views
# ViewSet for ExpressRegistration
class ExpressRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ExpressRegistration.objects.all()
    serializer_class = ExpressRegistrationSerializer
