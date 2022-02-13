from aiogram import types, Dispatcher
from create_bot import dp


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("fffffff")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

