"""
텔레그램 bot 기능을 활용하여 메시지 보내기
"""

# python-telegram-bot==v13.15 
import telegram
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('TELEGRAM_TOKEN')
id = os.environ.get('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")

# python-telegram-bot==v20.3
# https://www.inflearn.com/questions/737370/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-%EB%B4%87-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%98%A4%EB%A5%98-%EC%A7%88%EB%AC%B8%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4
# import asyncio
# import telegram
# from dotenv import load_dotenv
# import os

# load_dotenv()

# async def main(): #실행시킬 함수명 임의지정
#     token = os.environ.get('TELEGRAM_TOKEN')
#     id = os.environ.get('TELEGRAM_CHAT_ID')
    
#     bot = telegram.Bot(token = token)
#     await bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")

# asyncio.run(main()) #봇 실행하는 코드