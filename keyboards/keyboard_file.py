from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.utils.keyboard import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove 


def cycles() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Круглый карман", callback_data="round_pocket")
    kb.button(text="Радиусный карман", callback_data="radius_pocket")
    kb.button(text="Прямоугольный карман", callback_data="rectangular_pocket")
    kb.button(text="Фрезерование плоскости", callback_data="milling _plane")
    kb.button(text="Коническая резьба", callback_data="conical_thread")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def cycles_calculator() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Циклы")
    kb.button(text="Калькуляторы")
    kb.button(text="Назад")
    kb.button(text="Помощь")
    kb.adjust(2)
  #  kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def calculator() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Расчет режимов резания", callback_data="cutting_mode")
    kb.button(text="Превод в десятичный угол", callback_data="degrees_decimal")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)



def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Курсы USD, CNY")
    kb.button(text="Расчет заготовки")
    kb.button(text="Циклы и Калькуляторы")
    kb.button(text="Помощь")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def metal_profile() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Круг", callback_data="Круг")
    kb.button(text="Квадрат", callback_data="Квадрат")
    kb.button(text="Труба", callback_data="Труба")
    kb.button(text="Лист", callback_data="Лист")
    kb.button(text="Шестигранник", callback_data="Шестигранник")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
