from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storages = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storages)
