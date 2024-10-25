from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from mathematics.calculators import exchange_rate
from keyboards.inline import cycles, calculator, metal_profile
from keyboards.reply import cycles_calculator, get_yes_no_kb
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message): 
    await message.answer("Нажмите на необходимую Вам кнопку👇", 
                         reply_markup=get_yes_no_kb())
    

@router.message(F.text == "Курсы USD, CNY")
async def answer_yes(message: Message):
    dollar, yuan = exchange_rate()
    await message.answer(f"Доллар = {dollar}, Юань = {yuan}")


@router.message(F.text == "Циклы и Калькуляторы")
async def answer_no(message: Message):
    await message.answer("Нажмите на необходимую Вам кнопку👇",
        reply_markup=cycles_calculator())


@router.message(F.text == "Циклы")
async def answer_no(message: Message):
    await message.answer("Выберите Цикл👇",
            reply_markup=cycles())
    

@router.message(F.text == "Калькуляторы")
async def answer_no(message: Message):
    await message.answer("Выберите Калькулятор👇",
            reply_markup=calculator())


@router.message(F.text == "Назад")
async def answer_no(message: Message):
    await message.answer("Нажмите на необходимую Вам кнопку👇",
        reply_markup=get_yes_no_kb())
    

@router.message(F.text == "Помощь")
async def answer_no(message: Message):
    await message.answer("Если бот не работает отправьте команду '/start'",
        reply_markup=get_yes_no_kb())

    
@router.message(F.text == "Расчет заготовки")
async def answer_no(message: Message):
    await message.answer("Выберите профиль👇",
        reply_markup=metal_profile())
