from aiogram.utils import executor
from Handlers import client
from create_bot import dp

# async def on_startup():
# print("Bot started")


client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True)  # on_startup=on_startup
# test 11
