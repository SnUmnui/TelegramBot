
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg == 'hello':
        await msg.reply("world")
    elif msg == 'world':
        await msg.reply("hello")
    else:
        await msg.reply("error")