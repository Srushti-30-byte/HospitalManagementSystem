from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanySettlement
from .serializers import CompanySettlementSerializer


# Create your views here.
# Company Settlement Views
# ViewSet for Company Settlement
class CompanySettlementViewSet(viewsets.ModelViewSet):
    queryset = CompanySettlement.objects.all()
    serializer_class = CompanySettlementSerializer
