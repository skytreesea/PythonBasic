#말뭉치 기본 분석 우리가 아는 시에서 명사만 추출하기 
from konlpy.tag import *
from konlpy.corpus import kolaw
import re
kkma = Kkma()
hannanum = Hannanum()
print(kolaw.fileids())
ok = Okt()
with open(r'C:\Users\ERC\Documents\GitHub\PythonBasic\words\friends101.txt','r') as f:
    scripts = f.read()
    
new = re.split(r'[\:\.\!\?]', scripts)
new = [i for i in new if re.search('get',i)]
for i in new:
    print(i)
    