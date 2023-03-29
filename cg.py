from selenium import webdriver
from selenium.webdriver.common.by import By

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 구글 검색 페이지 열기
driver.get('https://www.google.com')

# 검색어 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('디자인 제작 툴')
search_box.submit()

# 검색 결과 추출
results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

for result in results:
    link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
    title = result.find_element(By.CSS_SELECTOR, 'h3').text
    if 'top' not in title.lower():  # 제목에 없는 경우에만 출력
        print(link, title)

# 브라우저 종료
driver.quit()
