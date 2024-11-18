from rest_framework import serializers


class CheckIDSerializer(serializers.Serializer):
    telegram_id = serializers.CharField()
