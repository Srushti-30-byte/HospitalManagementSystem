from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import OPDRefund
from .serializers import OPDRefundSerializer


# Create your views here.
# OPD Refund Views
# ViewSet for OPDRefund
class OPDRefundViewSet(viewsets.ModelViewSet):
    queryset = OPDRefund.objects.all()
    serializer_class = OPDRefundSerializer
