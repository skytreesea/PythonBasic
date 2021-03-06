#네이버 사전 예문 크롤링 기본형
import os , re, datetime, random, csv
import pandas as pd 
import requests
from bs4 import BeautifulSoup as bs
# words를 늘리면 단어 뜻과 예문 출력이 가능함
words=['example','greatest','vindictive','patriotic','strategy','abundant','adjacent','recall']
# 아래 주소에 단어만 더하면 단어 뜻과 예문이 든 페이지로 이동
total = {}
for word in words:
    url='https://endic.naver.com/search.nhn?sLn=kr&query='+ word
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup = bs(requests.get(url, headers = headers).text, 'lxml')
    element = []
    for i in soup.find_all('span', {'class':'fnt_k05'})[:3]:
        element.append(i.text)
    for text in soup.find_all('span', {'class':'fnt_e09 _ttsText'})[:3]:
        element.append(text.text)
    total[word] = element

df = pd.DataFrame(total).transpose()
df.to_clipboard()