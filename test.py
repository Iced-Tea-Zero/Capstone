from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 검색어
search_query = '디자인 제작 툴'

for page in range(1, 13):
    # 구글 검색 페이지 열기
    url = f'https://www.google.com/search?q={search_query}&start={(page - 1) * 10}'
    driver.get(url)
    time.sleep(10)

    # 검색 결과 추출
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    for result in results:
        # 사이트 제목
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        if 'top' in title.lower() or 'best' in title.lower() or '가지' in title.lower() or 'sm' in title.lower() \
                or '잡코리아' in title.lower() or '티타임즈' in title.lower() or '비교' in title.lower() or 'yes24' in title.lower() \
                or '사용법' in title.lower() or '비슷한' in title.lower() or '브런치' in title.lower() or '블로그' in title.lower()\
                or '기사' in title.lower() or '뉴스' in title.lower():  # 제목에 포함된 경우에는 출력하지 않음
            continue

        # 사이트 링크
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if 'tistory' in link or 'blog' in link or 'cafe' in link or 'news' in link or 'magazine' in link\
                or 'youtube' in link or 'category' in link or 'html' in link or 'inflearn' in link:
            continue
        # else 'com' not in link or 'net':

        # 사이트 설명 (날짜 형식을 없앰/만약 태그가 없을 경우, 예외처리하고 넘어가도록 구현)
        try:
            desc = result.find_element(By.CLASS_NAME, 'VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf').text
            new_desc = ''.join([i for i in desc if not i.isdigit() or i == ""])
        except NoSuchElementException:
            print("Element not found.")

        # 전체 출력
        print(" ", title, link, new_desc, sep='\n')

# 브라우저 종료
time.sleep(10)
driver.quit()