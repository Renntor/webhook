import telebot
from telebot import types
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os


load_dotenv()


app = FastAPI()

API = os.environ.get("BOT_API")
bot = telebot.TeleBot(API)

# WEBHOOK = f'/bot/{os.environ.get("BOT_API")}'

def hi(m):
    print(f'Hi, my name is {m}')
# @app.get('/')
# def test():
#     return {"hello world"}

# @app.on_event('startup')
# async def on_startup():
#     webhook = await

# @app.post(WEBHOOK)
# async def bot_webhook(update: dict):
#     pass

@bot.message_handler(func=lambda message: True)
def listening(message: types.Message):
    print(message.text)
    hi(message.text)

bot.polling()
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)