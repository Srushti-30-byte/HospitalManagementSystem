from rest_framework import serializers
from .models import OPDRefund


class OPDRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPDRefund
        fields = "__all__"
