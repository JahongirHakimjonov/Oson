from apps.oson.models import BotUsers
from apps.users.models import User


def update_or_create_user(
        telegram_id,
        username=None,
        first_name=None,
        last_name=None,
        is_active=True,
):
    """
    Update or create a user in the BotUsers model.

    :param telegram_id: User's Telegram ID
    :param username: User's username
    :param first_name: User's first name
    :param last_name: User's last name
    :param is_active: User's activity status
    """
    bot_user, created = BotUsers.objects.update_or_create(
        telegram_id=telegram_id,
        defaults={
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "is_active": is_active,
        },
    )
    if created:
        user = User.objects.create_user(telegram_id=telegram_id, password=f"password_{telegram_id}")
        user.bot_user = bot_user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.save()

        return user.tokens()