from aiogram.utils import executor
from aiogram import types, Dispatcher
from Handlers import student, admin, entrant, other
from KeyBoard import kb_student, mainMenu, abityrient_kb, choice_dep
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot

# async def on_startup():
# print("Bot started")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "hhhh", reply_markup=mainMenu)

@dp.message_handler(Text(equals="Студенту"))
async def student_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Студенту", reply_markup=kb_student)

@dp.message_handler(Text(equals="Абітурієнту"))
async def entrant_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Абітурієнту", reply_markup=abityrient_kb)

@dp.message_handler(Text(equals="dep"))
async def deps(message: types.Message):
    await bot.send_message(message.from_user.id, "deps", reply_markup=choice_dep)

@dp.message_handler(Text(equals="Назад"))
async def back_size(message: types.Message):
    await bot.send_message(message.from_user.id, "Назад", reply_markup=mainMenu)


other.register_handlers_other(dp)
student.register_handlers_client(dp)
entrant.register_handlers_entrant(dp)

executor.start_polling(dp, skip_updates=True)  # on_startup=on_startup

