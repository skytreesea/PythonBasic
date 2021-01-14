from bs4 import BeautifulSoup as bs
import requests,re
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=469&aid=0000571690'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')

for i in soup.find('strong',{'class':'media_end_summary'}):
    print(i)
