from aiogram.utils import executor
from create_bot import dp
from Handlers import starter_hendler, student, admin, entrant
# async def on_startup():
# print("Bot started")


starter_hendler.register_handlers(dp)
#student.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True)  # on_startup=on_startup
# test 11
