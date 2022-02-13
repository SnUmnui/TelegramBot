from aiogram import types, Dispatcher


#@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

#@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("fffffff")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])