from aiogram import types, Dispatcher
from Handlers.parser.parser_pdf import parser_pdf
from KeyBoard import abityrient_kb


# @dp.message_handler(commands=['raiting'])
async def raiting_student_handler(message: types.Message):
    search_item = 'admission rules'
    raiting = parser_pdf(search_item)
    await message.answer(raiting)


async def contact_handler(message: types.Message):
    await message.answer("contact +380668698666")


def register_handlers_ab(dp: Dispatcher):
    #dp.register_message_handler(process_start_command, commands=['start'])
    #dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_chat_join_request_handler(raiting_student_handler, commands=['r'])
    dp.register_message_handler(contact_handler, commands=['c'])
    #dp.register_message_handler(kb_comand)
