from aiogram.utils import executor
from aiogram import types, Dispatcher
from Handlers import student, admin, entrant, other
from KeyBoard import kb_student, mainMenu, abityrient_kb, choice_dep
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from sqlighter import SQLighter

# async def on_startup():
# print("Bot started")

db = SQLighter('db.db')
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    await bot.send_message(message.from_user.id, "hhhh", reply_markup=mainMenu)

@dp.message_handler(Text(equals="Студенту"))
async def student_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Студенту", reply_markup=kb_student)

@dp.message_handler(Text(equals="Абітурієнту"))
async def entrant_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Абітурієнту", reply_markup=abityrient_kb)

@dp.message_handler(Text(equals="Відділення"))
async def deps(message: types.Message):
    await bot.send_message(message.from_user.id, "Відділення", reply_markup=choice_dep)

@dp.callback_query_handler(text="dep_1")
async def dep_1(callback : types.CallbackQuery):
    await callback.message.answer(""
                                  "Головний корпус:\n"
                                  "\nіндекс - 79035, м. Львів,"
                                  "\nтел/факс: 270-20-50"
                                  "\nЕлектронна пошта: techcol@litech.net"
                                  "\nInternet адреса: http://techcol.com.ua"
                                  "")

@dp.callback_query_handler(text="dep_2")
async def dep_2(callback1 : types.CallbackQuery):
    await callback1.message.answer(""
                                   "Навчальний корпус № 2:\n"
                                   "\nіндекс - 79071, м. Львів,"
                                   "\nвул. Пулюя, 30 (бічна вул. Наукова),"
                                   "\nтел.: 264-66-61, 265-93-67."
                                   "")

@dp.callback_query_handler(text="dep_3")
async def dep_2(callback1 : types.CallbackQuery):
    await callback1.message.answer(""
                                   "Навчальний корпус №3\n"
                                   "\nіндекс - 81750, Львівська область,"
                                   "\nм. Ходорів, вул. Грушевського, 3,"
                                   "\nтелефони: (3239) 5-32-32, 5-34-61."
                                   "")

@dp.message_handler(Text(equals="Назад"))
async def back_size(message: types.Message):
    await bot.send_message(message.from_user.id, "Назад", reply_markup=mainMenu)



student.register_handlers_client(dp)
entrant.register_handlers_entrant(dp)

executor.start_polling(dp, skip_updates=True)  # on_startup=on_startup

