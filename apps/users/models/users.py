from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.shared.models import AbstractBaseModel
from apps.users.managers import UserManager


class RoleChoices(models.TextChoices):
    ADMIN = "ADMIN", _("Admin")
    USER = "USER", _("Foydalanuvchi")
    MODERATOR = "MODERATOR", _("Moderator")


class User(AbstractUser, AbstractBaseModel):
    telegram_id = models.BigIntegerField(unique=True, verbose_name=_("Telegram ID"))
    bot_user = models.ForeignKey(
        "oson.BotUsers",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user",
        verbose_name=_("Bot foydalanuvchisi"),
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_("Telefon raqami"),
    )
    username = models.CharField(
        max_length=100,
        verbose_name=_("Foydalanuvchi nomi"),
    )
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default=RoleChoices.USER,
        verbose_name=_("Role"),
    )

    USERNAME_FIELD = "telegram_id"
    # REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.phone}"
            if self.phone
            else str(_("Foydalanuvchi"))
        )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.telegram_id
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")
        ordering = ["-created_at"]
        db_table = "users"
        indexes = [
            models.Index(fields=["telegram_id"]),
            models.Index(fields=["username"]),
        ]

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
