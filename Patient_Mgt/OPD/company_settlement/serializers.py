from rest_framework import serializers
from .models import CompanySettlement


class CompanySettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySettlement
        fields = "__all__"
