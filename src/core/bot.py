from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery
from core.config import load_config
from static.dictionary import greeting_text, help_text
from utils.keyboard import gen_markup_keyboard
config = load_config(".env")
bot = AsyncTeleBot(token=config.tg_bot.token)


@bot.message_handler(commands=["start"])
async def start_message(message: Message) -> None:
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


@bot.message_handler(commands=["help"])
async def help_message(message: Message) -> None:
    user_name = message.from_user.full_name
    text = await help_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


@bot.message_handler(commands=["chose_cycle"])
async def chose_cycle(message: Message) -> None:
    await bot.send_message(message.from_user.id,
                           "Выберите нужный цикл!",
                           reply_markup=gen_markup_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == "circle")
async def callback_query_circle_pocket(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text="Yes")
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word
    func_generato()"""


@bot.callback_query_handler(func=lambda call: call.data == 'rectangle')
async def callback_query_rectangle_pocket(call: CallbackQuery) -> None:
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_2
    func_generato()
    return
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        user_id = message.from_user.id
        if message.text.lower() == 'end':
            bot.send_message(message.from_user.id, 'Прерываю цикл!')
            return
        number, erorrs = func_error(message.text, user[user_id].number_dict["number"])
        user[user_id].number_dict["number"] = number
        if erorrs != None:
            bot.send_message(message.from_user.id, erorrs)
        if number <= len(user[user_id].conditions['kelb']) -1:
            bot.send_message(message.from_user.id, user[user_id].conditions['kelb'][number])
    """
    await bot.answer_callback_query(call.id, text="Yes")


@bot.callback_query_handler(func=lambda call: call.data == 'radius')
async def callback_query_radius_pocket(call: CallbackQuery) -> None:
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_3
    func_generato()
            if user[user_id].conditions['kelb'] == word or user[user_id].conditions['kelb'] == word_2 or user[user_id].
            conditions['kelb'] == word_3:
            '''Условие для записи G-кода'''
            if number > 0:
                user[user_id].text_nc["text"] += f"#{number} = {message.text}\n"
            if number >= len(user[user_id].conditions["kelb"]):
                gen_text = generating_file(user[user_id].conditions['kelb'], user_id)
                bot.send_message(message.from_user.id, gen_text)
                return
    """
    await bot.answer_callback_query(call.id, text="Yes")


@bot.callback_query_handler(func=lambda call: call.data == 'cut_setting')
async def callback_query_radius_pocket(call: CallbackQuery) -> None:
    """
           user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_4
           elif user[user_id].conditions['kelb'] == word_4:
            '''Условие деля записи режимов резания'''
            if number > 0:
                user[user_id].working_dict["list"].append(message.text)
            if number >= len(user[user_id].conditions["kelb"]):
                turnovers, supply = mathematics(user[user_id].working_dict["list"])
                if supply != None:
                    bot.send_message(message.from_user.id, f'число оборотов = {turnovers} \nПодача = {supply}')
                else:
                    bot.send_message(message.from_user.id, turnovers)
                return"""
    await bot.answer_callback_query(call.id, text='Yes')


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


@bot.callback_query_handler(func=lambda call: True)
async def echo_callback_query(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text='all')
