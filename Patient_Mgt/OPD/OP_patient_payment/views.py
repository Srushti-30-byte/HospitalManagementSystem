from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import OP_patient_payment
from .serializers import OP_patient_paymentSerializer


# Create your views here.
# OP Patient Payment Views
# ViewSet for OP Patient Payment
class OP_patient_paymentViewSet(viewsets.ModelViewSet):
    queryset = OP_patient_payment.objects.all()
    serializer_class = OP_patient_paymentSerializer
