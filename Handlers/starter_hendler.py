from aiogram import types, Dispatcher
from Handlers.parser.parser_pdf import parser_pdf
from KeyBoard import kb, kb_student, abityrient_kb
from Handlers import student, admin, entrant
from create_bot import dp, bot



async def bot_message(message: types.Message):
    if message.text == 'Студент':
        await bot.send_message(message.from_user.id, 'Студенту', reply_markup=kb_student)
        await message.delete()
        student.register_handlers_client(dp)
# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=kb)

    # await bot.send_message(message.from_user.id, reply_markup=abityrient_kb)
    # entrant.register_handlers_ab(dp)



# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("------------------------"
                         "\nВиберіть одну з команд:"
                         "\n/start"
                         "\n/ra"
                         "\n------------------------")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(bot_message)
    #dp.register_message_handler(students)
