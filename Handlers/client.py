from aiogram import types, Dispatcher
from Handlers.parser.parser_raiting import parser_rait
from KeyBoard.client_kb import kb_client
from create_bot import bot
raiting = parser_rait()


# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!".format(message.from_user), reply_markup=kb_client)


async def bot_message(message: types.Message):
    if message.text == 'Рейтинг студентів':
        await message.reply(raiting)
    elif message.text == 'Контакти':
        await message.reply('контакти')
# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("------------------------"
                        "\nВиберіть одну з команд:"
                        "\n/start"
                        "\n/raiting"
                        "\n------------------------")

# @dp.message_handler(commands=['Рейтинг студентів'])
async def process_raiting_command(message: types.Message):
    pass

# @dp.message_handler(commands=['Росклад заннять'])


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(bot_message)
    #dp.register_message_handler(process_raiting_command, commands=['Рейтинг студентів'])

