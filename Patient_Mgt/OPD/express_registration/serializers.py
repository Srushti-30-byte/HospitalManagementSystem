from rest_framework import serializers
from .models import ExpressRegistration


class ExpressRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressRegistration
        fields = "__all__"
