from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

admission_rules = KeyboardButton('Правила прийому')
cost_education = KeyboardButton('Вартість навчання')
back = KeyboardButton('Назад')


abityrient_kb = ReplyKeyboardMarkup(resize_keyboard=True)
abityrient_kb.row(admission_rules, cost_education).add(back)