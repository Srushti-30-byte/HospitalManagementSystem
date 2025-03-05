from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import FollowUpList
from .serializers import FollowUpListSerializer


# Create your views here.
# Followup List Views
# ViewSet for Followup List
class FollowupListViewSet(viewsets.ModelViewSet):
    queryset = FollowUpList.objects.all()
    serializer_class = FollowUpListSerializer
