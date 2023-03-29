from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 검색어
search_query = '디자인 제작 툴'

for page in range(1, 11):
    # 구글 검색 페이지 열기
    url = f'https://www.google.com/search?q={search_query}&start={(page-1)*10}'
    driver.get(url)
    time.sleep(10)

    # 검색 결과 추출
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    for result in results:
        # 사이트 제목
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        # 사이트 링크
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        # 사이트 설명 (만약 태그가 없을 경우, 예외처리하고 넘어가도록 구현)
        try:
            desc = result.find_element(By.CLASS_NAME, 'VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf').text
        except NoSuchElementException: 
            print("Element not found.")

        # 전체 출력
        print(" ", title, link, desc, sep='\n')

# 브라우저 종료
time.sleep(10)
driver.quit()

