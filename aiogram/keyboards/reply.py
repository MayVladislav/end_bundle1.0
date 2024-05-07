from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class user_reply:
    start_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='VPN'),
                KeyboardButton(text='Помощь и инструкции'),
            ],
            [
                KeyboardButton(text='О пользователе'),
                KeyboardButton(text='О нас'),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='A u mad'
    )

    vpn_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Получить конфигурацию VPN'),
                KeyboardButton(text='Назад 💎'),
            ],
            #[
            #    KeyboardButton(text='Оплата')
            #]
        ],
        resize_keyboard=True,
        input_field_placeholder='A u mad BRO'
    )

    return_menu_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='В начало')
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='A u mad'
    )
    del_keyboard = ReplyKeyboardRemove()

    support_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Инструкция Android'),
                KeyboardButton(text='Инструкция Windows'),
            ],
            [
                KeyboardButton(text='Инструкция iOS'),
                KeyboardButton(text='Контакт помощи')
            ],
            [
                KeyboardButton(text='В главное меню')
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder='A u mad'
    )
