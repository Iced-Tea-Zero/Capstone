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

print(title_list)

# 데이터 추가-> for 문 추가하기
for i in range(len(title_list)):
    title = title_list[i]
    link = link_list[i]
    detail = detail_list[i]
    number = number_list[i]
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