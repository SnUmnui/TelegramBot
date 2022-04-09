from aiogram import types, Dispatcher
from Handlers.parser.parser_pdf import parser_pdf
from KeyBoard import kb_client
# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=kb_client)

# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("------------------------"
                        "\nВиберіть одну з команд:"
                        "\n/start"
                        "\n/raiting"
                        "\n------------------------")

# @dp.message_handler(commands=['raiting'])
async def kb_comand(message: types.Message):
    if message.text == 'Рейтинг студентів':
        search_item = 'admission rules'
        raiting = parser_pdf(search_item)
        await message.answer(raiting)
    elif message.text == 'Рахунок для оплати':
        await message.answer("bill")
    elif message.text == 'Контакти':
        await message.answer("contact +380668698666")

    else:
        if message.text == 'admin':
            return
        else:
            await message.delete()




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(kb_comand)
