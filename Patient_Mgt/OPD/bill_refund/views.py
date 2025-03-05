from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import BillRefund
from .serializers import BillRefundSerializer


# Create your views here.
# Bill Refund Views
# ViewSet for BillRefund
class BillRefundViewSet(viewsets.ModelViewSet):
    queryset = BillRefund.objects.all()
    serializer_class = BillRefundSerializer
