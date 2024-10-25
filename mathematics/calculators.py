import requests
from math import *



def exchange_rate():
    """Функция берет из цетробанка валюту доллар и юань"""
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    return data['Valute']['USD']['Value'], data['Valute']['CNY']['Value']


def cutting_mode(speed, diameter, number_teeth, tooth_pitch):
    """Функция считает режимы резания"""
    n = (1000 * float(speed))/(3.14 * float(diameter))
    f = float(number_teeth) * float(tooth_pitch) * n
    return f'Число оборотов = {int(n)}об/мин, Подача = {int(f)}мм/мин 👍'


def angle_decimal(corner, minute, second, radius):
    """Минуты-секунды в десятичное значение и считает координаты радиуса и угла"""
    ugol = int(corner) + int(minute)/60 + int(second)/3600
    osX = float(radius) * cos(radians(ugol))
    osY = float(radius) * sin(radians(ugol))
    return f'Угол равен = {round(ugol, 4)}, Ось X = {round(osX, 4)}, Ось Y = {round(osY, 4)} 👍'