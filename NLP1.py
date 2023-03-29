from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 검색어
search_query = '디자인 제작 툴'

# 리스트 선언
new_desc_list = []

# 파일 경로 지정
file_path = "my_list.txt"

for page in range(1, 13):
    # 구글 검색 페이지 열기
    url = f'https://www.google.com/search?q={search_query}&start={(page-1)*10}'
    driver.get(url)
    time.sleep(10)

    # 검색 결과 추출
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    for result in results:
        try:
            desc = result.find_element(By.CLASS_NAME, 'VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf').text
            new_desc = ''.join([i for i in desc if not i.isdigit() or i == ""])
        except NoSuchElementException:
            new_desc = "Element not found."

        new_desc_list.append(new_desc)

# 파일 열기 (쓰기 모드)
with open(file_path, "w", encoding="utf-8") as f:
    # 리스트의 각 요소를 파일에 쓰기
    for item in new_desc_list:
        f.write(str(item) + "\n")

# 브라우저 종료
time.sleep(10)
driver.quit()

# print(new_desc_list)
# num_items = len(new_desc_list)
# print(num_items)