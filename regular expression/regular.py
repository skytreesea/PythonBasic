import re

#전화번호 
variables = "02-1123-2235, 012-1222-5566, upan@upan.com, idontknow@upan.com, 121212-2233445, 231211-4212345"
# 전화번호 찾기 
print(re.findall('\d+-\d+-\d+', variables))
# 주민등록번호 찾기 
print(re.findall('\d+-\d+', variables))
# 이메일 주소 찾기 
print(re.search(r'[a-z]@[a-z\.]', variables))

print(re.findall(r'[a-z]+@[a-z\.]+', variables))

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
hangul= re.findall('[가-힣]+',a_html)
# 정규식으로 href 내용만 추출하기 
for i in href:
    print(i) # 따옴표까지 같이 출력하기 
    print(i[5:]) # 
    print(i[5:].strip('\"')) 
# 정규식으로 한글로 된 변수만 추출하기 
for i in hangul:
    print(i)

