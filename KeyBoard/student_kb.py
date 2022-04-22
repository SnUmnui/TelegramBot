from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

raiting = KeyboardButton('Рейтинг студентів')
bill = KeyboardButton('Рахунок для оплати')
contact = KeyboardButton('Контакти')

kb_student = ReplyKeyboardMarkup()
kb_student.add(raiting).add(bill).add(contact)