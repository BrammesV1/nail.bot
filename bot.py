import telebot
from telebot import types

TOKEN = '7827196968:AAHyoI5PbqbYEiTEgwvQimBj3li0_UxkVmE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_prices = types.KeyboardButton("Цены")
    btn_photos = types.KeyboardButton("Фотоработы")
    btn_location = types.KeyboardButton("Где нахожусь")
    btn_zapic = types.KeyboardButton("Записаться")
    markup.add(btn_prices, btn_photos)
    markup.add(btn_location, btn_zapic)

    bot.send_message(message.chat.id, "Привет! Меня зовут Влада, я мастер маникюра в Домодедово \nРабота на дому - уютно, чисто, с заботой о тебе. \nПриятные цены, качество - как в салоне. \nАкция - 20% на первый визит или парафинотерапия в подарок! \nниже выбери, что тебя интересует", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Цены")
def show_prices(message):
    bot.send_message(message.chat.id, "Вот мои цены")
    bot.send_photo (message.chat.id, 'AgACAgIAAxkBAAMdaCkM5pCItekK_4VXSLSjVZLhV20AAnz2MRtu4khJqoznzgQMKIoBAAMCAAN5AAM2BA')

@bot.message_handler(func=lambda message: message.text == "Где нахожусь")
def show_location(message):
    bot.send_message(message.chat.id, "Я нахожусь в г. Домодедово, Улица Лунная, дом 1к1.")

@bot.message_handler(func=lambda message: message.text == "Записаться")
def show_zapic(message):
    bot.send_message(message.chat.id, "Запись осуществляется через мастера @Mevlaaaa")

@bot.message_handler(func=lambda message: message.text == "Фотоработы")
def show_photo(message):
    bot.send_message(message.chat.id, "Вот примеры работ:")
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMfaCkNU5b3Y45E21qiSQpxs9rZ08kAAn72MRtu4khJirwOHvQ3OFUBAAMCAAN5AAM2BA')  # Фото 1
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMgaCkNUwvuQcsAAZMYH4n5nBNLCaI8AAKA9jEbbuJISdt0BX5Csl5mAQADAgADeQADNgQ') # Фото 2
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMhaCkNU-0uGvbY3rnZ-ZJLrcns8O8AAn_2MRtu4khJVmCCixLlOaABAAMCAAN5AAM2BA')  # Фото 3
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMiaCkNU1ZxAAGvsU9R1Lhr1QABvcbtNwACgfYxG27iSElLLbFOwROJZQEAAwIAA3kAAzYE') # Фото 4

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    bot.send_message(message.chat.id, f"File ID этой фотки:\n{file_id}")
bot.infinity_polling()