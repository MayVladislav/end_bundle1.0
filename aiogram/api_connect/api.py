from datetime import datetime
from io import BytesIO

from PIL import Image
import requests

base_url = 'http://38.180.156.31:64199/api/v1/'
token = '7347e11a8a186b6b5e77f30a99b1cec04026d6ab'


def GetList():
    url = base_url + 'get_vpn_list/'
    request = requests.get(url, headers={'Authorization': 'Token ' + token})
    if request.status_code == 200:
        data = request.json()
        return data


def GetLastElement():
    url = base_url + 'get_last_item/'
    request = requests.get(url, headers={'Authorization': 'Token ' + token})
    if request.status_code == 200:
        data = request.json()
        return data


def get_time_expired(time):
    date_obj = datetime.fromisoformat(time)
    if date_obj == 'None':
        formatted_date = "Не ограничен"
    else:
        formatted_date = date_obj.strftime("%d-%m-%Y")

    return formatted_date


def get_type(typ):
    type_ = typ
    if type_ == 1:
        type_ = 'Vless'
    elif type_ == 2:
        type_ = 'Shadowsocks'
    return type_


def get_photo_url(photo_id):
    photo_url_ = photo_id
    if photo_url_ is not None:
        return 'https://i.imgur.com/RMHR01K.png'


def RemoveLastElement():
    url = base_url + 'remove_last_item/'
    try:
        remove = requests.delete(url, headers={'Authorization': 'Token ' + token})
    except requests.exceptions.ConnectionError:
        remove = 'error'


def generate_qr_code():
    try:
        url = 'https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=123'
        return url
    except Exception as e:
        return e




