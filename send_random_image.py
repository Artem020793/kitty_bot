from telegram import Bot

import requests


bot = Bot(token='5737884728:AAGkFQ1hU13b18XVZqpDnpfJ7YitIacXXgM')

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
chat_id = 1839333183
random_cat_url = response[0].get('url')
bot.send_photo(chat_id, random_cat_url)