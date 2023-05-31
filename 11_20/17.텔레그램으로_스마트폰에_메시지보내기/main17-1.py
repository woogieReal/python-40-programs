"""
API Token을 이용하여 bot의 ID 알아내는 코드 만들기
"""

# python-telegram-bot==v13.15 
import telegram
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('TELEGRAM_TOKEN')
bot = telegram.Bot(token=token)
print(bot)


# python-telegram-bot==v20.3
# https://www.inflearn.com/questions/737370/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-%EB%B4%87-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%98%A4%EB%A5%98-%EC%A7%88%EB%AC%B8%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4
# import asyncio
# import telegram
# from dotenv import load_dotenv
# import os

# load_dotenv()

# async def main(): #실행시킬 함수명 임의지정
#     token = os.environ.get('TELEGRAM_TOKEN')
#     bot = telegram.Bot(token=token)
#     print(bot)
    
#     updates = await bot.getUpdates()
#     print(updates)
#     for u in updates:
#         print(u.message)

# asyncio.run(main()) #봇 실행하는 코드