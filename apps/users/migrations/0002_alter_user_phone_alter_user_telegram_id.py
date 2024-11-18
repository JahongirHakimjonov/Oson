# Generated by Django 5.0.8 on 2024-11-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="Telefon raqami"),
        ),
        migrations.AlterField(
            model_name="user",
            name="telegram_id",
            field=models.CharField(
                default=1, max_length=100, unique=True, verbose_name="Telegram ID"
            ),
            preserve_default=False,
        ),
    ]
