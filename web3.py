from selenium import webdriver
from selenium.webdriver.common.by import By
import time

plusUrl = input('검색어를 입력하세요: ')
url="https://www.similarweb.com/website/" + plusUrl


# 웹드라이버 실행
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

# 클래스 이름을 사용해 해당 엘리먼트를 찾고, 텍스트를 가져옵니다.
engagement_list_item_value = driver.find_element(By.CLASS_NAME, 'engagement-list__item-value').text

print(engagement_list_item_value)

# 웹드라이버 종료
driver.quit()