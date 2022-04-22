from aiogram import types, Dispatcher
from Handlers.parser.parser_pdf import parser_pdf
from KeyBoard import kb_student
from create_bot import dp, bot



# @dp.message_handler(commands=['raiting'])
async def raiting_student_handler(message: types.Message):
    search_item = 'admission rules'
    raiting = parser_pdf(search_item)
    await message.answer(raiting)


async def contact_handler(message: types.Message):
    await message.answer("contact +380668698666")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(raiting_student_handler, commands=['Рейтинг студентів'])
    dp.register_message_handler(contact_handler, commands=['Контакти'])

