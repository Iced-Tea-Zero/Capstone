from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 검색어
search_query = '디자인 제작 툴'

for page in range(1, 13):
    # 구글 검색 페이지 열기
    url = f'https://www.google.com/search?q={search_query}&start={(page-1)*10}'
    driver.get(url)
    time.sleep(10)

    # 검색 결과 추출
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    for result in results:
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        print(title, link)
        # desc = result.find_element(By.CLASS_NAME, 'Z26q7c UK95Uc').text
        # print(title, link, desc)

# 브라우저 종료
time.sleep(10)
driver.quit()

