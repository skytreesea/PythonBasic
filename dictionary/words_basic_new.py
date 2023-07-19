#네이버 사전 예문 크롤링 기본형
import os , re, datetime, random, csv
import pandas as pd 
import requests
from bs4 import BeautifulSoup  
# words를 늘리면 단어 뜻과 예문 출력이 가능함 
url = 'https://www.wordreference.com/enko/exquisite'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
url = 'http://quotes.toscrape.com/' 
soup = BeautifulSoup(requests.get(url, verify=False, headers = headers).text, 'html.parser')

print(soup.find('div',{"id":"articleWRD"}))