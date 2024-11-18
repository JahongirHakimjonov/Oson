from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.users.serializers import CheckIDSerializer

User = get_user_model()


class CheckIDView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CheckIDSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["phone"]
        exists = User.objects.filter(email=email).exists()
        return JsonResponse({"status": not exists})
