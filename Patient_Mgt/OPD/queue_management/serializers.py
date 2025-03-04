from rest_framework import serializers
from .models import QueueManagement


class QueueManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueManagement
        fields = "__all__"
