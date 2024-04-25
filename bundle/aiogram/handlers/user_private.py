import datetime
import time

import requests
from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import InputFile, FSInputFile

import config
from api_connect.api import GetList, get_time_expired, get_type, GetLastElement, RemoveLastElement
from keyboards.reply import user_reply
from filters.user_private_filter import MyAdminFilter

bot = Bot(token='6220269058:AAEjFkYsFX5NqfIIV_1IqJK6_iFnQCsUp2k')
user_private_router = Router()


@user_private_router.message(F.text == 'В начало')
@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        '''Здравствуйте! 👋🏼
        
Это бот установки VPN free 🤖
Осталось нажать всего пару кнопок, чтобы установить VPN 🎯
    
Попробуйте наш VPN сервис - это бесплатно!🕊️''',
        reply_markup=user_reply.start_keyboard
    )


@user_private_router.message(F.text == 'VPN')
async def vpn(message: types.Message):
    await message.answer('Выбирите конфигурацию VPN', reply_markup=user_reply.vpn_keyboard)


@user_private_router.message(F.text == 'Получить конфигурацию VPN')
async def vpn_post(message: types.Message):
    data = GetLastElement()
    print(data)
    for i in data:
        user_name = i['user_name']
        date_expire = i['date_expired']
        url = i['url']
        # photo_url = i['photo_url']
        type_ = i['type']

        date_expired = get_time_expired(date_expire)
        type_ = get_type(type_)
        # photo_url = get_photo_url(photo_url)

        RemoveLastElement()

        user = message.from_user
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        current_time = datetime.datetime.now()

        payload = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "config_name": user_name,
            "time_exp": date_expire,
            "time_take": current_time
        }
        api_url = "http://38.180.156.31:8000/api/v1/add_user_info/"
        response = requests.post(api_url, data=payload,)

        #if response.status_code == 201:
        #    await message.answer("Данные успешно отправлены на удаленный API.")
        #else:
        #    await message.answer("Произошла ошибка при отправке данных на удаленный API.")

        # if photo_url is not None:
        #    await message.answer('QR код')
        #    await message.answer_photo(photo_url)

        return await message.answer(
                                    f'''
Имя пользователя: {user_name}

Срок действия: {date_expired}

Адрес конфигурации: <a href='{url}'>{url}</a>

Тип соединения: {type_}''',
                                    parse_mode='HTML',
                                    reply_markup=user_reply.support_keyboard)

# @user_private_router.message(F.text == 'Получить конфигурацию VPN')
# async def vpn_post(message: types.Message):
#    await message.answer('Ваша конфигурация', reply_markup=user_reply.support_keyboard)
#    path = 'C:/Users/izi89/Downloads/ATLANTA_US_VPN.ovpn'
#    file = FSInputFile(path)
#    await message.answer_document(file)


#@user_private_router.message(F.text == 'Оплата')
#async def Payment(message: types.Message):
#    await message.answer_invoice('Покупка', 'Покупка конфигурации VPN', 'invoice', config.PAY_TOKEN, 'RUB', [types.LabeledPrice(label='Buying', amount=100*100)])


@user_private_router.message(F.text == 'Помощь')
@user_private_router.message(Command('help'))
async def support(message: types.Message):
    await message.answer('Инструкция по установке конфигурации', reply_markup=user_reply.support_keyboard)


@user_private_router.message(F.text == 'О пользователе')
@user_private_router.message(Command('about_me'))
async def echo(message: types.Message):
    await message.answer(str(message.from_user.id) + ' ' + str(message.from_user.full_name))


@user_private_router.message(F.text == 'Инструкция iOS')
async def text(message: types.Message):
    await message.answer(
        '''
Шаг 1.. Установите приложение <a href='https://apps.apple.com/ru/app/openvpn-connect-openvpn-app/id590379981'>OpenVPN</a> в App Store 📲
Шаг 2.. Откройте присланный файл конфигурации, нажмите «поделиться с приложением OpenVPN
Шаг 3.. Добавьте файл в приложение OpenVPN и включите VPN
            ''',
        parse_mode='HTML',
        reply_markup=user_reply.start_keyboard),


@user_private_router.message(F.text == 'Инструкция Android')
async def text(message: types.Message):
    await message.answer(
        '''
Шаг 1.. Выберите страну нажав кнопку «Выбор страны» 🌎
Шаг 2.. Загрузите полученный конфигурационный файл на устройство 💾
Шаг 3.. Установите приложение <a href='https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=ru&gl=US'>OpenVPN</a> в Google Play 📲
Шаг 4.. Запустите приложение OpenVPN и добавьте скаченный файл конфигурации ранее из папки Telegram File
            ''',
        parse_mode='HTML',
        reply_markup=user_reply.start_keyboard),


@user_private_router.message(F.text == 'Инструкция Windows')
async def text(message: types.Message):
    await message.answer(
        '''
Шаг 1.. Скачайте и установите <a href='https://openvpn.net/vpn-client/'>OpenVPN</a> с официального сайта
Шаг 2.. Загрузите полученный конфигурационный файл на устройство 💾
Шаг 3.. Откройте скаченный файл в через приложение OPENVPN и нажмите "Connect"
            ''',
        parse_mode='HTML',
        reply_markup=user_reply.start_keyboard),


@user_private_router.message(F.photo)
async def photo(message: types.Message):
    await message.answer_photo('https://free-png.ru/wp-content/uploads/2023/01/free-png.ru-128.png')


@user_private_router.message(F.text == 'О нас')
async def text(message: types.Message):
    await message.answer('VPN free <3')


@user_private_router.message(F.text == 'Контакт помощи')
async def text(message: types.Message):
    await message.answer('Контакт помощи @Ffffff27', reply_markup=user_reply.start_keyboard)


@user_private_router.message(F.text)
async def text(message: types.Message):
    await message.answer('Перевод в главное меню', reply_markup=user_reply.start_keyboard)
