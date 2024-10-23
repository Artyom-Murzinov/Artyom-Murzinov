from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from logic import *
from graphic_explan.dictonary import *

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    argument = message.text
    text, jpg =  data_generator(user[message.from_user.id].user_id, 
                                user[message.from_user.id].conditions['cycle_calc'], 
                                argument)
    print(message.from_user.full_name, message.from_user.id, message.text)
    if jpg == None: await message.answer(text)
    elif jpg == 1: await message.answer_document(FSInputFile('O0001.nc'), caption = text)
    else: await message.answer_photo(photo = FSInputFile(jpg), caption = text)


@router.callback_query(F.data)
async def send_random_value(callback: CallbackQuery):
    print(callback.from_user.full_name, callback.from_user.id, callback.data)
    user[callback.from_user.id] = User(callback.from_user.id)
    user[callback.from_user.id].conditions['cycle_calc'] = callback.data
    text, jpg = data_generator(callback.from_user.id, callback.data, argument = 0)
    if jpg != None:
        await callback.message.answer_photo(photo = FSInputFile(jpg), caption = text)
    else:
        await callback.message.answer(text=text)

    #Удаляю инлайн клавиатуру    
    await callback.message.delete()
    