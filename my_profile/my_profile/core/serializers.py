from rest_framework import serializers

from core.models import Subscriber


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Subscriber.objects.create(**validated_data)