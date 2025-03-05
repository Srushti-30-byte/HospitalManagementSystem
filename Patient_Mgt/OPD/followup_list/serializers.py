from rest_framework import serializers
from .models import FollowUpList


class FollowUpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpList
        fields = "__all__"
