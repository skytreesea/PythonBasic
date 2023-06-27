import re, os

test = "안녕하세요. 제 이름은 김창현입니다. 이메일 주소는 skytreesea@gmail.com 이고요. 전화번호는 010-4140-7296입니다."
#이메일 주소 
print(re.search('[a-z]+@[a-z\.]+', test).group())
#전화번호
print(re.search('\d+-\d+-\d+', test).group())

with open(r"C:\Users\skytr\Documents\GitHub\PythonBasic\words\littleprinceEnglish.txt",'r') as f:
    script = f.read()

# 특수문자를 일반문자처럼 인식하게 하기 \
# 인용구 안 표현만 모으기 
print(re.findall("\".+\"", script)[:10])

# 질문만 모으기 
print(re.findall("\".+\?\"", script)[:10])
