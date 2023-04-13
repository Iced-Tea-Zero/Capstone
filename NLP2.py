# 파일 -> NLP

import khaiii
import khaiii

# khaiii 분석기 생성
khaiii_inst = khaiii.KhaiiiApi()

# 분석할 텍스트 입력
text = "한글 텍스트를 형태소 분석하는 예시입니다."

# 형태소 분석
khaiii_inst.analyze(text)

# 분석 결과 출력
for word in khaiii_inst:
    print(word)









# list1 = []
#
# with open("my_list.txt", "r", encoding="utf-8") as f:
#     my_list = f.readlines()
#
# list1 = [s.replace('.', '').replace('—', '').replace('·', '').replace('/', '').replace(':', '') for s in map(str, my_list)]
#
# for item in list1:
#     print(item)c