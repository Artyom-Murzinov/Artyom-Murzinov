from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from core.config import load_config
from static.dictionary import greeting_text, help_text
from utils.keyboard import gen_markup_keyboard
config = load_config(".env")
bot = AsyncTeleBot(token=config.tg_bot.token)


@bot.message_handler(commands=["start"])
async def start_message(message: Message) -> None:
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=["help"])
async def help_message(message: Message) -> None:
    user_name = message.from_user.full_name
    await bot.send_message(message.from_user.id, "chose_cycle")


@bot.message_handler(commands=["chose_cycle"])
async def chose_cycle(message):
    await bot.send_message(message.from_user.id,
                           "Выберите нужный цикл!",
                           reply_markup=gen_markup_keyboard())


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
