from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

student = KeyboardButton('Студенту')
entrant = KeyboardButton('Абітурієнту')
dep = KeyboardButton('dep')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.row(student, entrant).add(dep)