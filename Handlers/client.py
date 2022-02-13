from aiogram import types, Dispatcher
from Handlers.parser.parser_raiting import parser_rait


raiting = parser_rait()


# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("------------------------"
                        "\nВиберіть одну з команд:"
                        "\n/start"
                        "\n/raiting"
                        "\n------------------------")

# @dp.message_handler(commands=['raiting'])
async def process_raiting_command(message: types.Message):
    await message.reply(raiting)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_raiting_command, commands=['raiting'])
