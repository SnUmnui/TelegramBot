from aiogram.utils import executor
from aiogram import types, Dispatcher
from create_bot import dp
from Handlers import student, admin, entrant
from KeyBoard import kb_student, kb, abityrient_kb
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot

# async def on_startup():
# print("Bot started")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=kb)
    if message.text == 'Студент':
        student.register_handlers_client(dp)
    # await bot.send_message(message.from_user.id, reply_markup=abityrient_kb)
    # entrant.register_handlers_ab(dp)

@dp.message_handler(Text(equals="Студент"))
async def student_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Студенту", reply_markup=kb_student)

@dp.message_handler(Text(equals="Абітурієнт"))
async def entrant_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Абітурієнт", reply_markup=abityrient_kb)

@dp.message_handler(Text(equals="Назад"))
async def back_siza(message: types.Message):
    await bot.send_message(message.from_user.id, "Назад", reply_markup=kb)

student.register_handlers_client(dp)
entrant.register_handlers_ab(dp)

executor.start_polling(dp, skip_updates=True)  # on_startup=on_startup
# test 11
