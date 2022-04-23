from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

student = KeyboardButton('Студент')
entrant = KeyboardButton('Абітурієнт')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(student, entrant)