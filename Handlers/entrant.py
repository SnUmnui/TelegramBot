from aiogram import types, Dispatcher
from Handlers.parser.parser_pdf import parser_pdf
from aiogram.dispatcher.filters import Text
from KeyBoard import kb
from create_bot import dp, bot

# @dp.message_handler(commands=['raiting'])
async def ruls(message: types.Message):
    search_item = 'admission rules'
    raiting = parser_pdf(search_item)
    await message.answer(raiting)


async def bill(message: types.Message):
    await message.answer("contact +380668698666")

#async def back(message: types.Message):
    #bot.send_message(message.from_user.id, "back", reply_markup=kb)

def register_handlers_ab(dp: Dispatcher):
    dp.register_chat_join_request_handler(ruls, Text(equals="Правила прийому"))
    dp.register_message_handler(bill, Text(equals="Вартість навчання"))
    #dp.register_message_handler(back, Text(equals="Назад"))