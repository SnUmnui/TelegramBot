from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

raiting = KeyboardButton('Рейтинг студентів')
bill = KeyboardButton('Рахунок для оплати')
contact = KeyboardButton('Контакти')

kb_client = ReplyKeyboardMarkup()
kb_client.add(raiting).add(bill).add(contact)