from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

my_list = []
web_list = []

file_path = "number.txt"

with open('link_list_short.txt', 'r') as f:
    lines = f.readlines()
    my_list = [line.strip() for line in lines]


for i in my_list:
    # 웹드라이버 생성
    driver = webdriver.Chrome()
    url="https://www.similarweb.com/website/" + i
    driver.get(url)
    time.sleep(5)

    # 클래스 이름을 사용해 해당 엘리먼트를 찾고, 텍스트를 가져옵니다.
    try:
        engagement_list_item_value = driver.find_element(By.CLASS_NAME, 'engagement-list__item-value').text
    except NoSuchElementException:
        engagement_list_item_value = "N/A"
    web_list.append(engagement_list_item_value)

    # 웹드라이버 종료
    driver.quit()

print(web_list)

# 파일 열기 (쓰기 모드) -> 사이트 설명만 txt 파일에 따로 저장하는 코드
with open(file_path, "w", encoding="utf-8") as f:
    # 리스트의 각 요소를 파일에 쓰기
    for item in web_list:
        f.write(str(item) + "\n")