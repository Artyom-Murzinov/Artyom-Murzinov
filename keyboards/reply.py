from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def cycles_calculator() -> ReplyKeyboardMarkup:
    """Клавиатура меню циклов и калькулятора"""
    kb = ReplyKeyboardBuilder()
    kb.button(text="Циклы")
    kb.button(text="Калькуляторы")
    kb.button(text="Назад")
    kb.button(text="Помощь")
    kb.adjust(2)
  #  kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    """клавиатура основного меню"""
    kb = ReplyKeyboardBuilder()
    kb.button(text="Курсы USD, CNY")
    kb.button(text="Расчет заготовки")
    kb.button(text="Циклы и Калькуляторы")
    kb.button(text="Помощь")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


