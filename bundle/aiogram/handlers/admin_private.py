import json
from aiogram.types import FSInputFile
import config
from keyboards.reply import user_reply
from aiogram import types, F
from aiogram import Router
from filters.user_private_filter import MyAdminFilter
from api_connect.api import *

admin_router = Router()
admin_router.message.filter(MyAdminFilter([492386687, ]))


@admin_router.message(F.text == 'admin')
async def admin(message: types.Message):
    data = GetList()
    print(data)
    for item in data:
        user_name = item['user_name']
        date_expired = item['date_expired']
        url = item['url']
        type_ = item['type']

        date_expired = get_time_expired(date_expired)
        type_ = get_type(type_)

        await message.answer('''
Имя пользователя: {user_name}
Срок действия: {date_expired}
Адрес конфигурации: <a href='{url}'>{url}</a>
Тип соединения: {type_}'''.format(
            user_name=user_name,
            date_expired=date_expired,
            url=url,
            type_=type_
        ), parse_mode='HTML', reply_markup=user_reply.return_menu_keyboard)


@admin_router.message(F.text == 'Оплата')
async def Payment(message: types.Message):
    await message.answer_invoice('Покупка', 'Покупка конфигурации VPN', 'invoice', config.PAY_TOKEN, 'RUB', [types.LabeledPrice(label='Buying', amount=100*100)])
