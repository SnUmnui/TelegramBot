from aiogram import types, Dispatcher
from sqlighter import SQLighter
from Handlers.parser.parser_pdf import parser_pdf

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
    search_item = 'admission rules'
    raiting = parser_pdf(search_item)

    await message.reply(raiting)

db = SQLighter('db.db')

# @dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id)
	else:
		db.update_subscription(message.from_user.id, True)
	
	await message.answer("Ви успішно підписались на розсилку!")

# @dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Ви і не були підписані")
	else:
		db.update_subscription(message.from_user.id, False)
		await message.answer("Ви успішно відписані від розсилки.")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_raiting_command, commands=['raiting'])
    dp.register_message_handler(subscribe, commands=['subscribe'])
    dp.register_message_handler(unsubscribe, commands=['unsubscribe'])
