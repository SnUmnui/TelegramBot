from aiogram import types, Dispatcher
from KeyBoard import choice_dep
from create_bot import dp, bot

async def dep_1(callback : types.CallbackQuery):
    await callback.message.answer("dep-1")

async def dep_2(callback1 : types.CallbackQuery):
    await callback1.message.answer("dep-2")


def register_handlers_other(dp: Dispatcher):
    dp.callback_query_handler(dep_1, text="dep_1")
    dp.callback_query_handler(dep_2, text="dep_2")