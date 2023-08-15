# 뷰티풀수프
from bs4 import BeautifulSoup 
import requests
from googletrans import Translator
def translate_text(text, target_lang='ko'):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=target_lang)
    return translation.text
    
#기본명령
url ='https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-future-of-middle-management'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')

r = 0 
#텍스트만 출력 
for i in soup.find_all('p'):
    print(f'{r}// {i.text} {translate_text(i.text)}\n')
    r += 1

 