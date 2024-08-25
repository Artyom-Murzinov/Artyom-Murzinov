from telebot.async_telebot import AsyncTeleBot
from core.config import load_config


config = load_config(".env")
bot = AsyncTeleBot(token=config.tg_bot.token)

