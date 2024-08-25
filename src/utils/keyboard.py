from telebot.types import InlineKeyboardMarkup

def gen_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Круглый карман")
    button_2 = KeyboardButton(text="Прямоугольный карман")
    button_3 = KeyboardButton(text="Радиусный карман")
    button_4 = KeyboardButton(text="Расчет режимов резания")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(button_1, button_2)
    keyboard.add(button_3, button_4)
    return keyboard
