#캠브리지사전 예문 크롤링 기본형
import os , re, datetime, random, csv
import pandas as pd 
import requests
from bs4 import BeautifulSoup as bs

url='https://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/%EC%98%81%EC%96%B4/lullaby'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')

for i in soup.find_all('span',{'class':'deg'}):
    print(i.text)

 