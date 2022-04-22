from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

student = KeyboardButton('Студент')
ab = KeyboardButton('Абітурієнт')

kb = ReplyKeyboardMarkup()
kb.add(student).add(ab)