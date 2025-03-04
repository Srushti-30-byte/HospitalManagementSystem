from rest_framework import serializers
from .models import PhoneAppointment


class PhoneAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAppointment
        fields = "__all__"
