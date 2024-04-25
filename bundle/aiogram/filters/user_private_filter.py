
from aiogram import types
from aiogram.filters import Filter


class MyAdminFilter(Filter):
    def __init__(self, admin_id: list[int]):
        self.admin_id = admin_id

    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in self.admin_id
