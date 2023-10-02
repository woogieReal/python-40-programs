from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import time
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Chrome()

send_message_list = []

while True:
    try:
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        driver.implicitly_wait(time_to_wait=10)
        titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
        message = ""
        for i in range(len(titles)):
            if "김치" in titles[i].text:
                message = titles[i].text + "\n" + urls[i].get_attribute('href')
                if message not in send_message_list:
                    print(message)
                    send_message_list.append(message)
                    token = os.environ.get('TELEGRAM_TOKEN')
                    id = os.environ.get('TELEGRAM_CHAT_ID')
                    bot = telegram.Bot(token)
                    bot.send_message(chat_id=id, text=message)
        
        time.sleep(60.0*5)
    except KeyboardInterrupt:
        break