import re
test = "\'나는 사람을 만났습니다.\'"
print(test.strip('\''))
variables = "02-1123-2235, 012-1222-5566, upan@upan.com, idontknow@upan.com, 121212-2233445, 231211-4212345"
print(re.findall('\d{6}-\d{7}', variables))

sentences = '''나는 이런 논문을 봤습니다(Great, 2020). 이런 문장을 많이 봅니다(James, 2012). 이런 인용구가 흔합니다(이동민, 2020).'''
# 문장 나누기 
split_sentences = re.split('\.', sentences)
print(re.findall('\(\D+\d{4}\)',sentences))
# 리스트 컴프리헨션을 통한 변형
results = re.findall('\(\D+\d{4}\)',sentences)
# 슬라이싱과 리스트컴프리헨션을 통한 변형
results = [i[1:-1] for i in results]
print(results)
print(split_sentences)