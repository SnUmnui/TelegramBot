from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

raiting = KeyboardButton('Рейтинг студентів')
bill = KeyboardButton('Рахунок для оплати')
contact = KeyboardButton('Контакти')
back = KeyboardButton('Назад')
kb_student = ReplyKeyboardMarkup(resize_keyboard=True)
kb_student.row(raiting, bill).add(contact).add(back)