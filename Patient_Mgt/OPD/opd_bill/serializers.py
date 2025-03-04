from rest_framework import serializers
from .models import OPDBill


class OPDBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPDBill
        fields = "__all__"
