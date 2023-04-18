from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome('/path/to/chromedriver')

# 검색어
search_query = ["문서 툴", "디자인 툴", "영상 툴"]

# 링크 저장 리스트
link_list = []

file_path = "linkList.txt"

for x in search_query:
    # 구글 검색 페이지 열기

    for page in range(1, 15):
        url = f'https://www.google.com/search?q={x}&start={(page - 1) * 10}'
        driver.get(url)
        time.sleep(20)

        # 검색 결과 추출
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

        for result in results:
            # 사이트 제목
            title = result.find_element(By.CSS_SELECTOR, 'h3').text

            if 'top' in title.lower() or 'best' in title.lower() or '가지' in title or '베스트' in title \
                    or '사용법' in title or 'tip' in title.lower() or '가이드' in title or '설명' in title\
                    or '비슷한' in title or '비교' in title or '추천' in title or '소개' in title\
                    or 'yes24' in title.lower() or '브런치' in title or '잡플래닛' in title\
                    or '씨넷코리아' in title or '예스폼' in title or '닥터주부' in title\
                    or '기사' in title or '뉴스' in title or '블로그' in title\
                    or '송파구' in title or '절약' in title or '이직' in title or '모집' in title\
                    or '고르기' in title or '선정하기' in title or '모음' in title:
                # 제목에 포함된 경우에는 출력하지 않음
                continue

            # 사이트 링크
            link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')

            if 'youtube' in link or 'inflearn' in link or 'epicgames' in link\
                    or 'news' in link.lower() or 'article' in link or 'articles' in link or 'magazine' in link\
                    or 'html' in link or 'tutorial' in link or 'sindohblog' in link or 'MSTRWeb' in link\
                    or 'survey' in link or 'kakaoenterprise' in link or 'lgcns' in link\
                    or 'marketsplash' in link or 'tistory' in link or '9multi' in link\
                    or 'wingsnote' in link or 'onoffmix' in link or 'airklass' in link\
                    or 'masocampus' in link or 'chrome' in link or 'microsoft' in link\
                    or 'besuccess' in link or 'apple.com' in link or 'segye' in link\
                    or 'instagram' in link or 'ciokorea' in link or 'dprime' in link:
                continue

            if 'com' not in link:
                continue
                if 'net' not in link:
                    continue
                    if 'co.kr' not in link:
                        continue
                        if 'io' not in link:
                            continue

            # 사이트 설명 (날짜 형식을 없앰/만약 태그가 없을 경우, 예외처리하고 넘어가도록 구현)
            try:
                desc = result.find_element(By.CLASS_NAME, 'VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf').text
                new_desc = ''.join([i for i in desc if not i.isdigit() or i == ""])
                new_desc = new_desc.replace(".", "")
                new_desc = new_desc.replace("—", "")
                new_desc = new_desc.replace("·", "")
            except NoSuchElementException:
                print("Element not found.")

            # 전체 출력
            print(" ", title, link, new_desc, sep='\n')

            link_list.append(link)

# 링크 txt 파일로 저장
with open(file_path, "w", encoding="utf-8") as f:
    # 리스트의 각 요소를 파일에 쓰기
    for item in link_list:
        f.write(str(item) + "\n")

# # 파일 열기 (쓰기 모드) -> 사이트 설명만 txt 파일에 따로 저장하는 코드
# with open(file_path, "w", encoding="utf-8") as f:
#     # 리스트의 각 요소를 파일에 쓰기
#     for item in new_desc_list:
#         f.write(str(item) + "\n")
#
# # 파일 열기 (쓰기 모드) -> 사이트 제목만 txt 파일에 따로 저장하는 코드
# with open(file_path_2, "w", encoding="utf-8") as f:
#     # 리스트의 각 요소를 파일에 쓰기
#     for item2 in new_title_list:
#         f.write(str(item2) + "\n")


# 브라우저 종료
time.sleep(10)
driver.quit()