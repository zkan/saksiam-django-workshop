from rest_framework import serializers

from .models import Profile, Subscriber


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Subscriber.objects.create(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
