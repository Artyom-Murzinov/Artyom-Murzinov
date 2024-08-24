import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import TeleBot
from math import *
bot = telebot.TeleBot 'X' # Токен, полученный от BotFather.


'''Списки и словари для работы заполнения текстового документа'''
word = ["Введите диаметр отверстия: ", "Введите глубину отверстия, пишется с отрицательным значением: ", 
        "Введите радиус фрезы: ", "Введите шаг фрезерования: ", 
        "Поверхность детали: ", "Коэффициент перекрытия фрезы, 1-полный диаметр: "]
word_2 = ["Введите длину кармана: ", "Введите ширину кармана: ", "Введите глубину кармана: ", 
          "Поверхность детали: ", "Введите шаг фрезерования: ", "Введите радиус фрезы: ", 
          "Коэффициент перекрытия фрезы: "]
word_3 = ["Введите ширину кармана: ", "Введите длину кармана в градусах: ", "Введите глубину кармана: ", 
          "Поверхность детали: ", "Начальный угол: ", "Средний радиус паза: ", "Введите радиус фрезы: ", 
          "Введите шаг фрезерования: ", "Коэффициент перекрытия фрезы: "]
word_4 = ['Введите скорость Vc', 'Введите диаметр фрезы D', 'Введите число зубев Z', 'Введите съем на зуб Fz']
number_dict = {'number': 0}
conditions = {'kelb': list}
text_nc = {"text": "% \nO0001 \n"}
working_dict = {'list': []}


def mathematics(number_list):
    n = (1000 * float(number_list[0]))/(3.14 * float(number_list[1]))
    f = float(number_list[2]) * float(number_list[3]) * n
    return int(n), int(f)


def generating_file(action):
    if action == word:
        action1 = "KK"   
    elif action == word_2:
        action1 = "PK"
    elif action == word_3:
        action1 = "RK"
    if action1 =='KK' or action1 =='PK' or action1 =='RK':
        new_code = open("O0001.nc", "w")
        with open(f"{action1.lower()}.txt", "r", encoding="utf-8") as pk:
            info = pk.read()
        new_code.write(text_nc['text'])
        with open("O0001.nc", "a") as new_code:
            new_code.write(info)
        text_nc["text"] += info
        return text_nc["text"]


def func_error(argumet, numb):
    '''Ловлю ошибку если на FLOAT'''
    try:
        float(argumet)
        numb += 1
        return numb, None
    except :
        return numb, 'Введите число'
    

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


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Выберите нужный цикл!",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )


def func_generato():
    '''Заполняю текстовый документ нужными параметрами'''
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        print(message.text)
        if message.text == 'end':
            bot.send_message(message.chat.id, 'Прерываю цикл!')
            return
        number, erorrs = func_error(message.text, number_dict["number"])
        number_dict["number"] = number
        if erorrs != None:
            bot.send_message(message.chat.id, erorrs)
        if number <= len(conditions['kelb']) -1:
            bot.send_message(message.chat.id, conditions['kelb'][number])
    ##############################################################################
        if conditions['kelb'] == word or conditions['kelb'] == word_2 or conditions['kelb'] == word_3:
            '''Условие для записи G-кода'''
            if number > 0:
                text_nc["text"] += f"#{number} = {message.text}\n"
            if number >= len(conditions["kelb"]):
                gen_text = generating_file(conditions['kelb'])
                bot.send_message(message.chat.id, gen_text) 
                text_nc["text"] = "% \nO0001 \n" 
        elif conditions['kelb'] == word_4:
            '''Условие деля записи режимов резания'''
            if number > 0:
                working_dict["list"].append(message.text)
            if number >= len(conditions["kelb"]):
                turnovers, supply = mathematics(working_dict["list"])
                bot.send_message(message.chat.id, f'число оборотов = {turnovers} \nПодача = {supply}') 
                working_dict["list"]= [] 
        return
    number_dict["number"] = 0        
    return

# Генераторы циклов!!!
@bot.message_handler(func=lambda message: message.text == "Круглый карман")
def echo_all(message):
    bot.send_message(message.chat.id, 'Отправьте любую БУКВУ')
    conditions['kelb'] = word   
    func_generato()    
    return


@bot.message_handler(func=lambda message: message.text == "Прямоугольный карман")
def echo_all(message):
    bot.send_message(message.chat.id, 'Отправьте любую БУКВУ')
    conditions['kelb'] = word_2
    func_generato()
    return


@bot.message_handler(func=lambda message: message.text == "Радиусный карман")
def echo_all(message):
    bot.send_message(message.chat.id, 'Отправьте любую БУКВУ')
    conditions['kelb'] = word_3
    func_generato()
    return


@bot.message_handler(func=lambda message: message.text == "Расчет режимов резания")
def echo_all(message):
    bot.send_message(message.chat.id, 'Отправьте любую БУКВУ')
    conditions['kelb'] = word_4
    func_generato()
    return



if __name__ == "__main__":
    print('Бот запущен')
    bot.infinity_polling()
