import re

# 입력 리스트
lst = ['서울대학교 대학원', '성균관대학교 대학원', '한양대학교 대학원', '고려대학교 교육대학원']

result = [elem.replace('학교.+?대학원', '') for elem in result]

print(result) 




