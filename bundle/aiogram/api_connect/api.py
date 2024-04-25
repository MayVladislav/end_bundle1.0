from datetime import datetime

import requests


def GetList():
    url = 'http://38.180.156.31:8000/api/v1/get_vpn_list/'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        return data


def GetLastElement():
    url = 'http://38.180.156.31:8000/api/v1/get_last_item/'
    request = requests.get(url)
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
    url = 'http://38.180.156.31:8000/api/v1/remove_last_item/'
    try:
        remove = requests.delete(url)
    except requests.exceptions.ConnectionError:
        remove = 'error'
