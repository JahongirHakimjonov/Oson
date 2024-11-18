from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView,
)

from apps.users.views import (
    RegisterView,
    CheckIDView,
    MeView,
    ResendView,
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/check/id/", CheckIDView.as_view(), name="check_phone"),
    path("auth/me/", MeView.as_view(), name="me"),
    path("auth/resend/", ResendView.as_view(), name="resend"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
