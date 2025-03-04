from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import QueueManagement
from .serializers import QueueManagementSerializer


# Create your views here.
# Express Registration Views
# ViewSet for ExpressRegistration
class QueueManagementViewSet(viewsets.ModelViewSet):
    queryset = QueueManagement.objects.all()
    serializer_class = QueueManagementSerializer
