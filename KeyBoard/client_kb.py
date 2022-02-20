from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

button_rainting = KeyboardButton('Рейтинг студентів')
button_contact = KeyboardButton('Контакти')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(button_rainting, button_contact)


# .add(button_schedule).add(button_contact)
