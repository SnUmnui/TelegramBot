from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_dep = InlineKeyboardMarkup(row_width=3)
dep_1 = InlineKeyboardButton(text="Головний корпус", callback_data="dep_1")
dep_2 = InlineKeyboardButton(text="Корпус №2", callback_data="dep_2")
dep_3 = InlineKeyboardButton(text="Корпус №3", callback_data="dep_3")

choice_dep.add(dep_1).add(dep_2).add(dep_3)

