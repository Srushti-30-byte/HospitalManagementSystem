from rest_framework import serializers
from .models import PhoneAppointment, PhoneAppointmentList


class PhoneAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAppointment
        fields = "__all__"


class PhoneAppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAppointmentList
        fields = "__all__"
