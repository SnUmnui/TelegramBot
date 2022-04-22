from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

admission_rules = KeyboardButton('Правила прийому')
cost_education = KeyboardButton('Вартість авчання')
#contact = KeyboardButton('Контакти')

abityrient_kb = ReplyKeyboardMarkup()
abityrient_kb.add(admission_rules).add(cost_education)