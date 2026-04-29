import telebot
from datetime import datetime
import pytz
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

last_reply = {}

TIMEZONE = pytz.timezone("Europe/Berlin")

def is_off_hours():
    now = datetime.now(TIMEZONE)
    return not (9 <= now.hour < 18)

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    if not is_off_hours():
        return

    chat_id = message.chat.id
    today = datetime.now(TIMEZONE).date()

    if last_reply.get(chat_id) == today:
        return

    text = """Hi! Our team is currently offline.

We’ll get back to you as soon as we’re back online 😊

Working hours: Monday–Friday, 9:00–18:00 CET."""

    bot.send_message(chat_id, text)
    last_reply[chat_id] = today

bot.infinity_polling()
