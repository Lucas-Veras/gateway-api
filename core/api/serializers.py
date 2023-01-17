from rest_framework import serializers

class ParameterSerializer(serializers.Serializer):
    parameter = serializers.CharField()
    