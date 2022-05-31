
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, dispatcher
from sqlighter import SQLighter
from Handlers.parser.paresr_news import check_news_update
import json
import asyncio
from datetime import datetime
from random import uniform
from time import sleep




async def subscribe():
	pass
async def unsubscribe():
	pass

db = SQLighter('db.db')
async def command_pars(wait_for, first_wait):
	await asyncio.sleep(first_wait)
	while True:
		subscriptions = db.get_subscriptions()
		if len(subscriptions) == 0:
			await asyncio.sleep(wait_for)
		else:
			fresh_news_dict = check_news_update()
			for s in subscriptions:

				id_ = s[1]
				status = s[2]
				if status == 1:
					for key, value in sorted(fresh_news_dict.items()):
						print("------------------------------")
						news = f"{value['title_news']}\n"
						links = value['url_news']
						link_button = InlineKeyboardMarkup()
						links = InlineKeyboardButton(text="Детальніше", url=value["url_news"])
						link_button.add(links)
						await bot.send_photo(id_, value['photo_news'], news, reply_markup=link_button)
				else:
					print("unsub")
				await asyncio.sleep(wait_for)

loop = asyncio.get_event_loop()
loop.create_task(command_pars(uniform(15,20), 5))