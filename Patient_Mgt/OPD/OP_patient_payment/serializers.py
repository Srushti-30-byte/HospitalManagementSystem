from rest_framework import serializers
from .models import OP_patient_payment


class OP_patient_paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OP_patient_payment
        fields = "__all__"
