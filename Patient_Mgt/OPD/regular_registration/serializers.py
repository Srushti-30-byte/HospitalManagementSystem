from rest_framework import serializers
from .models import RegularRegistration


class RegularRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularRegistration
        fields = "__all__"
