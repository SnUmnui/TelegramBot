from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_dep = InlineKeyboardMarkup(row_width=2)
dep_1 = InlineKeyboardButton(text="dep_1", callback_data="dep_1")
dep_2 = InlineKeyboardButton(text="dep_2", callback_data="dep_2")

choice_dep.insert(dep_1)
choice_dep.insert(dep_2)

