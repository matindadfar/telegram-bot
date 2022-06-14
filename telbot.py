import telebot
import requests
import time

Token = "your bot token"
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hey, this is the Btc_bot!\n what can i do for you today?")


@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message, "Hey there\n to use this bot please enter currency symbol!")


@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"{data['symbol']}price is{data['price']}")

    else:
        bot.reply_to(message, "you entered wrong symbol!")




# bot.infinity_polling()
while True:
    try:
        bot.polling()
    except:
        time.sleep(15)


