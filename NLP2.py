# 파일 -> NLP

from khaiii import KhaiiiApi
import pandas as pd

api = KhaiiiApi()

for w in api.analyze("안녕하세요. khaiii를 사용해봅시다."):
    print(w)


# list1 = []
#
# with open("my_list.txt", "r", encoding="utf-8") as f:
#     my_list = f.readlines()
#
# list1 = [s.replace('.', '').replace('—', '').replace('·', '').replace('/', '').replace(':', '') for s in map(str, my_list)]
#
# for item in list1:
#     print(item)