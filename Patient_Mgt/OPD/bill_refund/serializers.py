from rest_framework import serializers
from .models import BillRefund


class BillRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillRefund
        fields = "__all__"
