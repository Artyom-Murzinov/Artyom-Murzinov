from core.bot import bot
import asyncio
from custom_handlers.message import register_custom_message_handlers
from custom_handlers.callback import register_custom_callback_query_handlers

register_custom_message_handlers(bot)
register_custom_callback_query_handlers(bot)
asyncio.run(bot.polling())
