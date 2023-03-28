from urllib.parse import quote_plus
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색어를 입력하세요: ') # 이 부분은 우리가 키워드를 저장하는 식으로 바꾸는 게 나을 듯
url = baseUrl + quote_plus(plusUrl)

# chromedriver path input
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
driver.get(url)
driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html)

v = soup.select('.yuRUbf')
w = soup.select('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf')

for i in v:
    print(i.select_one('.LC20lb.DKV0Md').text) # 사이트 제목
    print(i.a.attrs['href']) # 사이트 링크
print()

for j in w:
    print(j.span.text) # 사이트 정보
    print(j.em.text)
print()

print('done')

driver.close()


# 1. span 값이 이상함
# 2. 첫 페이지만 끌고 옴 -> 모든 페이지를 다 보고 싶어서...
# 3. for 문을 보기 좋게 하나로 합치쟈 -> 배열 혹은 리스트로 저장해야 함
# 4. youtube나 뉴스로 적혀있으면 걸려야 함
# 5. 무료 / 공유 가능을 웹크롤링으로 만들 수 있음 (boolean 형식 T/F로!!)
# 6. DB에 저장
#
# import requests
# from bs4 import BeautifulSoup
#
# query = "디자인 제작 툴"
# url = f"https://www.google.com/search?q={query}"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
#
# results = []
# for g in soup.find_all('div', class_='r'):
#     anchors = g.find_all('a')
#     if anchors:
#         link = anchors[0]['href']
#         title = g.find('h3').text
#         description = g.find(class_='s').text
#         item = {
#             "title": title,
#             "link": link,
#             "description": description
#         }
#         results.append(item)
#
# print(results)