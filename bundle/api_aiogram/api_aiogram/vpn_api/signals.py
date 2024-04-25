from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VpnUserUseModel1
import asyncio
from aiogram import Bot


async def send_admin_notification(message):
    bot = Bot(token="6220269058:AAEjFkYsFX5NqfIIV_1IqJK6_iFnQCsUp2k")
    await bot.send_message(chat_id="492386687", text=message)


@receiver(post_save, sender=VpnUserUseModel1)
def create_vpn_user(sender, instance, created, **kwargs):
    if created:
        print("Vpn User Created")
        asyncio.run(send_admin_notification("Новая покупка конфигурации VPN"))
    else:
        print("Vpn User not Created")
