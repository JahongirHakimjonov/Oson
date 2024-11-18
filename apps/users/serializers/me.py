from rest_framework import serializers

from apps.users.models import User


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "telegram_id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "role",
            "created_at",
            "updated_at",
        ]
