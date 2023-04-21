import pymongo

# MongoDB 연결 생성
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 데이터베이스 선택
db = client["sitedb"]

# 컬렉션 선택
collection = db["textCol"]

with open('title_list.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    title_list = [line.strip() for line in lines]

with open('link_list.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    link_list = [line.strip() for line in lines]

with open('detail_list.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    detail_list = [line.strip() for line in lines]

with open('number.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    number_list = [line.strip() for line in lines]

with open('hashtags.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    hashtags_list = [line.strip() for line in lines]

rank_list = []
def str_to_num(string):
    if string[-1] == 'B':
        return float(string[:-1]) * 1e9
    elif string[-1] == 'M':
        return float(string[:-1]) * 1e6
    elif string[-1] == 'K':
        return float(string[:-1]) * 1e3
    else:
        return float(string)

for num_str in number_list:
    num = int(str_to_num(num_str))
    rank_list.append(num)

zipped_lists = zip(rank_list, title_list, link_list, detail_list, hashtags_list)
sorted_lists = sorted(zipped_lists, reverse=True)
rank_list, title_list, link_list, detail_list, hashtag_list = zip(*sorted_lists)

# 데이터 추가-> for 문 추가하기
for i in range(len(title_list)):
    title = title_list[i]
    link = link_list[i]
    detail = detail_list[i]
    number = rank_list[i]
    hashtag = hashtags_list[i]

    data = {
        "title": title,
        "link": link,
        "detail": detail,
        "number": number,
        "hashtag": hashtag
    }
    collection.insert_one(data)

client.close()