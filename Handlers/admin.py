from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text

class FSM_Admin(StatesGroup):
    tuition_bill_photo = State()
    description_tuition_bill = State()
   # news_tuition_bill_photo = State()
   # news_description_tuition_bill = State()


#@dp.message_handler(commands='admin', state=None)
async def enter_photo(message: types.Message):
    await FSM_Admin.tuition_bill_photo.set()
    await message.answer("send photo")


#@dp.message_handler(content_types=['photo'], state=FSM_Admin.tuition_bill_photo)
async def st1(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await message.answer("send description")
    await FSM_Admin.next()

#@dp.message_handler(state=FSM_Admin.description_tuition_bill)
async def st2(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    async with state.proxy() as data:
        await message.answer(str(data))

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ok')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(enter_photo, commands='admin', state=None)
    dp.register_message_handler(st1, content_types=['photo'], state=FSM_Admin.tuition_bill_photo)
    dp.register_message_handler(st2, state=FSM_Admin.description_tuition_bill)
    dp.register_message_handler(cancel, state="*", commands='cancel')
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state="*")

