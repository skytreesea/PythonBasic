#말뭉치 기본 분석 우리가 아는 시에서 명사만 추출하기 
from konlpy.tag import *
from konlpy.corpus import kolaw
kkma = Kkma()
hannanum = Hannanum()
print(kolaw.fileids())
ok = Okt()
 
c = kolaw.open('constitution.txt').read()

# 헌법 앞 부분에 있는 명사만 추출하기 
print(ok.nouns(c[:200]))
# kka(꼬꼬마)로 이춘수 꽃 형태소 추출하기
flower= '''내가 그의 이름을 불러 주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다

내가 그의 이름을 불러 주었을땐
그는 나에게로 와서
꽃이 되었다

내가 그의 이름을 불러준 것처럼
나의 이 빛깔과 향기에 알맞은
누가 나의 이름을 불러다오

그에게로 가서 나도
그의 꽃이 되고 싶다

우리들은 모두
무엇이 되고 싶다

나는 너에게로 너는 나에게로
잊혀지지 않는 하나의 의미가 되고 싶다.

'''
print(kkma.morphs(flower))