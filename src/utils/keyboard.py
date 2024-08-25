from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup_keyboard() -> InlineKeyboardMarkup:
    # Создаём объекты кнопок.
    button_1 = InlineKeyboardButton(text="Круглый карман", callback_data='circle')
    button_2 = InlineKeyboardButton(text="Прямоугольный карман", callback_data='rectangle')
    button_3 = InlineKeyboardButton(text="Радиусный карман", callback_data='radius')
    button_4 = InlineKeyboardButton(text="Расчет режимов резания", callback_data='cut_setting')
    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard
