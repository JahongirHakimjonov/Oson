from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from apps.bot.utils import update_or_create_user
from apps.users.serializers import (
    RegisterSerializer,
    ResendSerializer,
)
from apps.users.services.users import UserService


class RegisterView(APIView, UserService):
    permission_classes = [AllowAny]
    throttle_classes = [UserRateThrottle]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = update_or_create_user(
                telegram_id=serializer.data.get("telegram_id"),
                first_name=serializer.data.get("first_name"),
                last_name=serializer.data.get("last_name"),
                username=serializer.data.get("username"),
                is_active=True,
            )
            return Response(
                user,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendView(APIView, UserService):
    serializer_class = ResendSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get("phone")
        self.send_confirmation(self, phone)
        return Response(
            {"message": _(f"Confirmation code sent to {phone} phone number.")},
            status=status.HTTP_200_OK,
        )
