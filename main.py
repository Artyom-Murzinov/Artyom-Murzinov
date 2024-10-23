import asyncio
from aiogram import Bot, Dispatcher, types
from handlers import questions, different_types
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(questions.router, different_types.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    while True:
        try:
            print("Бот запущен!!!")
            asyncio.run(main())
        except:
            sleep(1)



