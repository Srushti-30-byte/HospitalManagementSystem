from rest_framework import serializers
from .models import CourierList, CourierDetails


class CourierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierList
        fields = "__all__"


class CourierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierDetails
        fields = "__all__"
