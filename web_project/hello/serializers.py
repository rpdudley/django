from rest_framework import serializers
from .models import LogMessage

class LogMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogMessage
        fields = '__all__'
