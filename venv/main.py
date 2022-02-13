from aiogram.utils import executor
from create_bot import dp, bot
from Handlers import client, admin, other
async def on_startup():
    print("Bot started")


client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

dlsfk;gjl;dskg;ds