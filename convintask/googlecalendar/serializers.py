from rest_framework import serializers

from .models import User, Event

class EventSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(max_length=50)
    event_timestamp = serializers.DateTimeField()
    class Meta:
        model = Event
        fields = ['event_name','event_timestamp']


class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['user_name']
