"""
텔레그램 bot 기능을 활용하여 메시지의 자동응답 보내는 코드 만들기
"""

# python-telegram-bot==v13.15 
import telegram
from dotenv import load_dotenv
import os
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

load_dotenv()

token = os.environ.get('TELEGRAM_TOKEN')
id = os.environ.get('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="자동응답 테스트 입니다. 안녕 또는 뭐해 를 입력하여 보세요")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text 
    if user_text == "안녕": 
        bot.send_message(chat_id=id, text="어 그래 안녕")
    elif user_text == "뭐해": 
        bot.send_message(chat_id=id, text="그냥 있어") 

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)