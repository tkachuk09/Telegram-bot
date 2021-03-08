import requests
from datetime import datetime
import telebot
from auth_data import token                                       # Import some useful libraries and modules

# Make a GET request to the API:

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]                      # Request sell price in convenient format
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

# Configure our Telegram-bot

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello, dear! Write the 'price' to find out the cost of BTC")

    @bot.message_handler(content_types=["text"])
    def send_message(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]                      # Get sell price in convenient format
                bot.send_message(
                        message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                    )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Oh..something went wrong..."
                )

        else:
              bot.send_message(message.chat.id, "What? Check the command and try again")

    bot.polling()

if __name__ == '__main__':
    get_data()
    telegram_bot(token)
