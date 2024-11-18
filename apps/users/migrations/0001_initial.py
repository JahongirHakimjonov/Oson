# Generated by Django 5.0.8 on 2024-11-18 10:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("oson", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SmsConfirm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.IntegerField(verbose_name="Kod")),
                (
                    "try_count",
                    models.IntegerField(default=0, verbose_name="Urinishlar soni"),
                ),
                (
                    "resend_count",
                    models.IntegerField(
                        default=0, verbose_name="Qayta yuborishlar soni"
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=255, verbose_name="Telefon raqami"),
                ),
                (
                    "expire_time",
                    models.DateTimeField(blank=True, null=True, verbose_name="Muddati"),
                ),
                (
                    "unlock_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Bloklanish vaqti"
                    ),
                ),
                (
                    "resend_unlock_time",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Qayta yuborish bloklanish vaqti",
                    ),
                ),
            ],
            options={
                "verbose_name": "SMS tasdiqlash",
                "verbose_name_plural": "SMS tasdiqlashlar",
                "db_table": "sms_confirm",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "telegram_id",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name="Telegram ID",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Telefon raqami"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=100, verbose_name="Foydalanuvchi nomi"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("USER", "Foydalanuvchi"),
                            ("MODERATOR", "Moderator"),
                        ],
                        default="USER",
                        max_length=20,
                        verbose_name="Role",
                    ),
                ),
                (
                    "bot_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to="oson.botusers",
                        verbose_name="Bot foydalanuvchisi",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Foydalanuvchi",
                "verbose_name_plural": "Foydalanuvchilar",
                "db_table": "users",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ResetToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "token",
                    models.CharField(max_length=255, unique=True, verbose_name="Token"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Foydalanuvchi",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tokenni tiklash",
                "verbose_name_plural": "Tokenni tiklash",
                "db_table": "reset_token",
            },
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["telegram_id"], name="users_telegra_d76140_idx"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(fields=["username"], name="users_usernam_baeb4b_idx"),
        ),
    ]
