import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommandScope, BotCommandScopeAllPrivateChats
from dotenv import find_dotenv, load_dotenv

from bot_cmd_list import private
from handlers.admin_private import admin_router
from handlers.user_private import user_private_router

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
