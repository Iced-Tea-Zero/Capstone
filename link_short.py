import re

with open('link_list.txt', 'r') as f:
    lines = f.readlines()
    my_list = [line.strip() for line in lines]

domains = []

for link in my_list:
    domain = re.search('//(.+?)/', link).group(1)
    domain = re.sub('^www\.', '', domain)
    domains.append(domain)

print(domains)

# 링크 파일 경로 지정
file_path ="link_list_short.txt"

# 파일 열기 (쓰기 모드) -> 사이트 링크를 다시 link_list.txt에 저장하는 코드
with open(file_path, "w", encoding="utf-8") as f:
    # 리스트의 각 요소를 파일에 쓰기
    for item in domains:
        f.write(str(item) + "\n")