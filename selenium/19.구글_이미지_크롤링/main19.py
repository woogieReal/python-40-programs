#!/usr/bin/env python
# coding: utf-8

# In[2]:


from webdriver_manager.chrome import ChromeDriverManager # 구글 크롬 드라이버의 자동설치를 위한 라이브러리를 불러옴
from selenium import webdriver # 크롬 드라이버의 제어를 위해 selenium 라이브러리를 불러옴

# 크롬 드라이버를 시작, 프로그램이 설치되지 않았다면 자동으로 설치
driver = webdriver.Chrome(ChromeDriverManager().install())

# 구글의 이미지 검색 사이트로 이동
URL='https://www.google.co.kr/imghp'
driver.get(url=URL)

# 사이트로 이동할 때까지 최대 10초 동안 기다림
driver.implicitly_wait(time_to_wait=10)


# In[5]:


from selenium.webdriver.common.keys import Keys # 키입력을 위한 라이브러리를 불러옴
from selenium.webdriver.common.by import By # CSS 선택을 위한 라이브러리를 불러옴

# 검색할 키워드인 "바다"를 입력하여 검색
elem = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[7]:


import time

# 바디 부분을 찾는다.
elem = driver.find_element(By.TAG_NAME, "body")

# 페이지 다운키를 60회 눌러 사진이 계속 보이도록 한다.
for i in range(60): 
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    # 중간에 [결과더보기] 버튼이 있다면 눌러서 계속 사진이 보이도록 한다. 
    driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click() 
    
    # [결과더보기] 버튼이 눌린 후 페이지 다운키를 60회 눌러 사진이 계속 보이도록 한다.
    for i in range(60): 
        elem.send_keys(Keys.PAGE_DOWN) 
        time.sleep(0.1) 
except: 
    pass


# In[8]:


links=[] 

# 이미지의 원소를 모두 찾는다.
images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print(' 찾은 이미지 개수:',len(links))


# 

# In[9]:


import urllib.request # 사진을 다운로드 받기 위해 라이브러리를 불러옴

for k,i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "/Users/woogie/Desktop/real/python-40-programs/11_20/19.구글_이미지_크롤링/사진다운로드/"+str(k)+".jpg")

print('다운로드 완료하였습니다.')

