from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def cycles() -> InlineKeyboardMarkup:
    """клавиатура Фрезерные циклы карманов"""
    kb = InlineKeyboardBuilder()
    kb.button(text="Круглый карман", callback_data="round_pocket")
    kb.button(text="Чистовой круглый карман", callback_data="finishing_round_pocket")
    kb.button(text="Радиусный карман", callback_data="radius_pocket")
    kb.button(text="Прямоугольный карман", callback_data="rectangular_pocket")
    kb.button(text="Чистовой прямоугольный карман", callback_data="finishing_rectangular_pocket")
    kb.button(text="Фрезерование плоскости", callback_data="milling _plane")
    kb.button(text="Фрезерование внутренней резьбы", callback_data="thread_milling")
    kb.button(text="Коническая резьба", callback_data="conical_thread")
#    kb.button(text="Гравировка текста", callback_data="engraving")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def calculator() -> InlineKeyboardMarkup:
    """Клавиатура калькуляторов"""
    kb = InlineKeyboardBuilder()
    kb.button(text="Расчет режимов резания", callback_data="cutting_mode")
    kb.button(text="Превод в десятичный угол", callback_data="degrees_decimal")
    kb.button(text="Фрезерная поворотная UFG", callback_data="UFG")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def metal_profile() -> InlineKeyboardMarkup:
    """Клавиатура металлопрофиля"""
    kb = InlineKeyboardBuilder()
    kb.button(text="Круг", callback_data="Круг")
    kb.button(text="Квадрат", callback_data="Квадрат")
    kb.button(text="Труба", callback_data="Труба")
    kb.button(text="Лист", callback_data="Лист")
    kb.button(text="Шестигранник", callback_data="Шестигранник")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
