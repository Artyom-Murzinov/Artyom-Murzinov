from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from core.config import load_config
from static.dictionary import greeting_text
config = load_config(".env")
bot = AsyncTeleBot(token=config.tg_bot.token)


@bot.message_handler(commands=["start"])
async def start_message(message: Message) -> None:
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text)


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    print("yes_echo")
    await bot.reply_to(message, message.text)
