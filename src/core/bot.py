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
    await bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=["help"])
async def help_message(message: Message) -> None:
    user_name = message.from_user.full_name
    await bot.send_message(message.from_user.id, "chose_cycle")


@bot.message_handler(commands=["chose_cycle"])
async def chose_cycle(message: Message) -> None:
    await bot.send_message(message.from_user.id,
                           "Выберите нужный цикл!",
                           reply_markup=gen_markup_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == "circle")
async def callback_query_circle_pocket(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text="Yes")


@bot.callback_query_handler(func=lambda call: call.data == 'rectangle')
async def callback_query_rectangle_pocket(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text="Yes")


@bot.callback_query_handler(func=lambda call: call.data == 'radius')
async def callback_query_radius_pocket(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text="Yes")


@bot.callback_query_handler(func=lambda call: call.data == 'cut_setting')
async def callback_query_radius_pocket(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text='Yes')


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


@bot.callback_query_handler(func=lambda call: True)
async def echo_callback_query(call: CallbackQuery) -> None:
    await bot.answer_callback_query(call.id, text='all')
