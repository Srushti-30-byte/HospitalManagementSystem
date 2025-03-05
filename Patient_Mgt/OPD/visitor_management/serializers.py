from rest_framework import serializers
from .models import VisitorDetails, VisitorList, VisitorPass


class VisitorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorDetails
        fields = "__all__"


class VisitorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorList
        fields = "__all__"


class VisitorPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorPass
        fields = "__all__"
