import telebot
import os
from dotenv import load_dotenv
from graphic_explan.dictonary import dictonary, user
from logika import*
from keyboards import*
from time import sleep
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

 
#Здесь бот оправляет клавиатуры пользователю
@bot.message_handler(commands = ["start"])
def start_message(message):
    bot.send_message(message.from_user.id, "НАЖМИТЕ НА КНОПКУ! 👇👇 'Циклы' либо 'Помощь'", 
                     reply_markup=reply_markup())  # Отправляем клавиатуру.
    

@bot.message_handler(func=lambda message: message.text == "Циклы")
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Нажмите на текст нужного вам цикла!👇",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )


@bot.message_handler(func=lambda message: message.text == "Курсы USD, CNY")
def start_message(message):
    usd, cny = currency()
    bot.send_message(message.chat.id, f"Доллар={usd}, Юань={cny}")


@bot.message_handler(func=lambda message: message.text == "Помощь")
def start_message(message):
    bot.send_message(message.chat.id, "Если бот не реагирует, попробуйте ещё раз отправить команду /start.")

# Логика заполнения переменных в G-коде
def func_generator():
    '''Заполняю текстовый документ нужными параметрами'''
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        try:  
            user_id = message.from_user.id
            print(message.from_user.first_name, message.text)
            number, erorrs = func_error(message.text, user[user_id].number_dict["number"], len(user[user_id].conditions['kelb']))
            user[user_id].number_dict["number"] = number
            if erorrs != None:
                bot.send_message(message.from_user.id, erorrs)
            if number <= len(user[user_id].conditions['kelb']) - 1:
                try:
                    msg = open(user[user_id].conditions['kelb'][number][1], '+rb')
                    bot.send_photo(message.chat.id, msg, caption = user[user_id].conditions['kelb'][number][0])
                except:
                    bot.send_message(message.chat.id, user[user_id].conditions['kelb'][number])
    ##############################################################################
            if user[user_id].conditions['kelb'] == dictonary["round_pocket"
                ] or user[user_id].conditions['kelb'] == dictonary["rectangular_pocket"
                ] or user[user_id].conditions['kelb'] == dictonary["radius_pocket"
                ] or user[user_id].conditions['kelb'] == dictonary["milling _plane"
                ] or user[user_id].conditions['kelb'] == dictonary["conical_thread"]:
                '''Условие для записи G-кода'''
                if number > 0 and erorrs == None:
                    user[user_id].text_nc["text"] += f"#{number} = {message.text}\n"
                if number == len(user[user_id].conditions["kelb"]):
                    generating_file(user[user_id].conditions['kelb'], user_id)
                    bot.send_document(message.from_user.id, document=open('O0001.nc', 'rb'))
            elif user[user_id].conditions['kelb'] == dictonary["cutting_mode"]:
                '''Условие для записи режимов резания'''
                if number > 0 and erorrs == None:
                    user[user_id].working_dict["list"].append(message.text)
                if number == len(user[user_id].conditions["kelb"]):
                    turnovers, supply = mathematics(user[user_id].working_dict["list"])
                    if supply != None:
                        bot.send_message(message.from_user.id, f'число оборотов = {turnovers} \nПодача = {supply}')
                    else:
                        bot.send_message(message.from_user.id, turnovers)
            elif user[user_id].conditions['kelb'] == dictonary["degrees_decimal"]:
                '''Условие записи преобразования угла и расчет координат'''
                if number > 0 and erorrs == None:
                    user[user_id].working_dict["list"].append(message.text)
                if number == len(user[user_id].conditions["kelb"]):
                    ugol, osy = decimal_angle(user[user_id].working_dict["list"])
                    if osy != None:
                        bot.send_message(message.from_user.id, f'Угол = {ugol} \nОсь Х = {osy[0]}, Ось У = {osy[1]}')
                    else:
                        bot.send_message(message.from_user.id, ugol)
        except Exception as er:
            print(er)   



@bot.callback_query_handler(func=lambda callback_query: True)
def dog_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    
    user_id = callback_query.from_user.id
    user[user_id] = User(user_id) 
    bot.send_message(callback_query.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = dictonary[callback_query.data]
    func_generator()


if __name__ == "__main__":
    while True:
        try:
            print('Бот запущен')
            bot.infinity_polling(none_stop=True)
        except:
            sleep(0.3) 
