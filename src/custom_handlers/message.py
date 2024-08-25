from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from static.dictionary import greeting_text, help_text
from utils.keyboard import gen_markup_keyboard


async def start_message(message: Message, bot: AsyncTeleBot) -> None:
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


async def help_message(message: Message, bot: AsyncTeleBot) -> None:
    user_name = message.from_user.full_name
    text = await help_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


async def chose_cycle(message: Message, bot: AsyncTeleBot) -> None:
    await bot.send_message(message.from_user.id,
                           "Выберите нужный цикл!",
                           reply_markup=gen_markup_keyboard())


async def echo_message(message, bot: AsyncTeleBot) -> None:
    await bot.reply_to(message, message.text)


def register_custom_message_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start_message, commands=["start"], pass_bot=True)
    bot.register_message_handler(help_message, commands=["help"], pass_bot=True)
    bot.register_message_handler(chose_cycle, commands=["chose_cycle"], pass_bot=True)
    bot.register_message_handler(echo_message,func=lambda message: True, pass_bot=True)
