from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import json
from time import strptime
import time
import datetime

"""
NEED client_secret.json in same script folder
"""

# google excel data imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# current date
curret_date = datetime.datetime.today().strftime('%d.%m.%Y')

#global
ask = 0

def get_sheet_data():
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
	client = gspread.authorize(creds)
	sheet = client.open("Telega").sheet1
	all_content = sheet.get_all_records()
	try:
		latest_post = all_content[0][curret_date]
	except KeyError:
		latest_post = [*all_content[0].values()][0]
	except:
		latest_post = "Ошибка сервера, попробуйте через несколько минут или обратитесь к администратору!"
	
	global ask
	ask += 1
	print("Asked: " + str(ask))
	return latest_post


token = "<YOUR TOKEN>"

bot = Bot(token=token)
dp = Dispatcher(bot) 
main_text = "Hi!\nЭто LasTTrade бот, созданный для публикации сигналов с сайта lasttrade.ru,"
main_text += "\nпросмотра различных котировок и других плюшек!\nСписок доступных команд:\n/start - приветственное сообщение, которое вы читаете"
main_text += "\n/help - выводит список всех доступных команд\n/crypto - выводит котировки некоторых криптовалют: BTC/USD, ETH/USD, ZEC/USD и другие"
main_text += "\n/lt - выводит последний пост сигналов с lasttrade.ru"

help_text = "Список ВСЕХ доступных команд:\n/start - приветственное сообщение\n/help - выводит список всех доступных команд"
help_text += "\n/crypto - выводит котировки некоторых криптовалют: BTC/USD, ETH/USD, ZEC/USD и другие\n/lt - выводит последний пост сигналов с lasttrade.ru"
help_text += "\n/6E или /eur - выводит котировки фьючерса EUR/USD (6E)"
help_text += "\n/contact - связаться с автором, выводит контактные данные"

def get_euro():
	try:
		eur_req = requests.get("http://www.cmegroup.com/CmeWS/mvc/Quotes/Future/58/G?pageSize=500&_=1526404120619")
		text_eur = eur_req.text
		obj = json.loads(text_eur)
		return obj["quotes"][0]["last"]
	except:
		return "Что-то пошло не так, попробуйте сделать запрос повторно, через 30 сек!"

def crypto_currency():
	try:
		list_cur_url = requests.get("https://api.exmo.com/v1/ticker/")
		main_response = json.loads(list_cur_url.text)
	
		btc_rate = "BTC: " + main_response["BTC_USD"]["buy_price"]
		bth_rate = "BTH: " + main_response["BCH_USD"]["buy_price"]
		eth_rate = "ETH: " + main_response["ETH_USD"]["buy_price"]
		etc_rate = "ETC: " + main_response["ETC_USD"]["buy_price"]
		zec_rate = "ZEC: " + main_response["ZEC_USD"]["buy_price"]
		ltc_rate = "LTC: " + main_response["LTC_USD"]["buy_price"]
		dash_rate = "DASH: " + main_response["DASH_USD"]["buy_price"]
		xrp_rate = "XRP: " + main_response["XRP_USD"]["buy_price"]

		full_text = btc_rate + "\n" + bth_rate + "\n" + eth_rate + "\n" + etc_rate + "\n" + zec_rate + "\n" + ltc_rate + "\n" + dash_rate + "\n" + xrp_rate + "\n"
		return full_text
	except:
		return "Что-то пошло не так, попробуйте сделать запрос повторно, через 30 сек!"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply(main_text)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
	await message.reply(help_text)

@dp.message_handler(commands=['crypto'])
async def send_crypto(message: types.Message):
	await message.reply(crypto_currency())

@dp.message_handler(commands=['lt'])
async def send_lt(message: types.Message):
	await message.reply(get_sheet_data())

@dp.message_handler(commands=['contact'])
async def send_contact(message: types.Message):
	await message.reply("Cвязаться с автором:\nSkype: Chantofvictory\nEmail: teamfm@ukr.net")
	
@dp.message_handler(commands=['6E', 'EURO', 'eur', 'euro'])
async def send_eur(message: types.Message):
	await message.reply(get_euro())

print("Bot started!")

if __name__ == '__main__':
	executor.start_polling(dp)
