from urllib.parse import quote_plus
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

from selenium import webdriver

from bs4 import BeautifulSoup
import requests

save1 =[]

plusUrl = input('원하는 사이트의 주소를 입력하세요 : ')
url = "https://www.similasrweb.com/website/" + plusUrl
headers = {'User-Agent': 'Mozilla/5.0'}

res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

v = soup.select('.wa-overview__title')
print(v.text)


# webpage = urlopen(res).read()
# print(webpage)
# soup = BeautifulSoup(res.text, "lxml")
#
# print(type(soup))
# print(soup.head)
# print(soup.body)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# # chromedriver path input
# driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
# driver.get(url)
# driver.implicitly_wait(10)
#
# html = driver.page_source
# soup = BeautifulSoup(html)
#
# v = soup.select('.wa-overview__title')
#
# print(v.text)
# print()
#
# print('done')
#
# driver.close()
