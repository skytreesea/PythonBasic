import re
#re에서는 findall과 sub을 알면 우리가 상상하는 거의 모든 일을 할 수 있다. 
#전화번호, 이메일주소, 가상 주민등록번호로 매일 정규식을 연습하면 프로그래밍시 요긴하게 사용할 수 있다. 
variables = "02-1123-2235, 012-1222-5566, upan@upan.com, idontknow@upan.com, 121212-2233445, 231211-4212345"
# 전화번호 찾기 
print(re.findall('\d+-\d+-\d+', variables))
# 주민등록번호 찾기 
print(re.findall('\d{6}-\d{7}', variables))
# 이메일 주소 찾기 
print(re.search(r'[a-z]@[a-z\.]', variables))
print(re.findall(r'[a-z]+@[a-z\.]+', variables))
test = "\'나는 사람을 만났습니다.\'"
print(test.strip('\''))
variables = "02-1123-2235, 012-1222-5566, upan@upan.com, idontknow@upan.com, 121212-2233445, 231211-4212345"
print(re.findall('\d{6}-\d{7}', variables))

#split을 통한 문장 나누기 
sentences = '''나는 이런 논문을 봤습니다(Great, 2020). 이런 문장을 많이 봅니다(James, 2012). 이런 인용구가 흔합니다(이동민, 2020).'''
# 문장 나누기 
split_sentences = re.split('\.', sentences)
print(split_sentences)

print(re.findall('\(\D+\d{4}\)',sentences))
# 리스트 컴프리헨션을 통한 변형
results = re.findall('\(\D+\d{4}\)',sentences)
# 슬라이싱과 리스트컴프리헨션을 통한 변형
results = [i[1:-1] for i in results]
print(results)

# a_html 이라는 변수로 실험 
a_html = '''
<li class="nav_item"><a href="https://dict.naver.com/" class="nav" data-clk="svc.dic">사전</a></li>
<li class="nav_item"><a href="https://news.naver.com/" class="nav" data-clk="svc.news">뉴스</a></li>
<li class="nav_item"><a href="https://finance.naver.com/" class="nav" data-clk="svc.stock">증권</a></li>
<li class="nav_item"><a href="https://land.naver.com/" class="nav" data-clk="svc.land">부동산</a></li>
<li class="nav_item"><a href="https://map.naver.com/" class="nav" data-clk="svc.map">지도</a></li>
<li class="nav_item"><a href="https://movie.naver.com/" class="nav" data-clk="svc.movie">영화</a></li>
<li class="nav_item"><a href="https://vibe.naver.com/" class="nav" data-clk="svc.vibe">VIBE</a>
<li class="nav_item"><a href="https://book.naver.com/" class="nav" data-clk="svc.book">책</a></li>
<li class="nav_item"><a href="https://comic.naver.com/" class="nav" data-clk="svc.webtoon">웹툰</a></li>
'''
href = re.findall('href=\"[a-z/\.:]+\"', a_html)
name= re.findall('>[가-힣A-Za-z]+<',a_html)

for i in href:
    print(i) 
#href=""는 불필요하니 없애고, url주소만 남겨놓고 싶음
#하나의 리스트만 남겨놓는 방법
#리스트 컴프리헨션
animal = ['토끼', '말','사슴', '코끼리','하마'] 
# 모든 요소에 '01'붙이고 싶을 때? 
animal = [i+'01' for i in animal]
#100 미만 숫자만 가진 리스트로 바꾸고 싶다면? 
numbers =[12,233,34,33,44,53]
numbers = [i for i in numbers if i < 100] # numbers의 각각 요소에 대하여 100보다 작을 경우에 list에 그대로 남겨두어라.
print(numbers)
#리스트 컴프리헨션 활용
# 정규식으로 href 내용만 추출하기 
for i in href:
    print(i) # 따옴표까지 같이 출력하기 
    print(i[5:]) # 
    print(i[5:].strip('\"')) 
    


href = [i[5:].strip('\"') for i in href]
name = [i[1:-1] for i in name]
# 정규식으로 한글로 된 변수만 추출하기 
new_total=[]
# 조금 복잡하지만 지금 우리가 알고 있는 지식으로 csv로 저장되는 형태 리스트로 변형
for i in range(len(name)):
    blank =[]
    blank.append(name[i])
    blank.append(href[i])
    new_total.append(blank)
    i += 1
import csv, os
os.chdir(r'D:\user\Documents\git hub\PythonBasic\csv')
# newline =''가 없으면 불필요한 공백을 한 행으로 인식하여 만듦
with open('save_info.csv','w', newline='') as f:
    a=csv.writer(f, delimiter=',')
    a.writerows(new_total)
