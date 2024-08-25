from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery


async def callback_query_circle_pocket(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text="Yes")
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word
    func_generato()"""


async def callback_query_rectangle_pocket(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_2
    func_generato()
    """
    await bot.answer_callback_query(call.id, text="Yes")


async def callback_query_radius_pocket(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_3
    func_generato()
    """
    await bot.answer_callback_query(call.id, text="Yes")


async def callback_query_cut_setting(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """
    user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_4
    func_generato()
        """
    await bot.answer_callback_query(call.id, text='Yes')


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text='all')


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(callback_query_circle_pocket,
                                        func=lambda call: call.data == "circle", pass_bot=True)
    bot.register_callback_query_handler(callback_query_rectangle_pocket,
                                        func=lambda call: call.data == 'rectangle', pass_bot=True)
    bot.register_callback_query_handler(callback_query_radius_pocket,
                                        func=lambda call: call.data == 'radius', pass_bot=True)
    bot.register_callback_query_handler(callback_query_cut_setting,
                                        func=lambda call: call.data == 'cut_setting', pass_bot=True)
    bot.register_callback_query_handler(echo_callback_query,
                                        func=lambda call: True, pass_bot=True)
