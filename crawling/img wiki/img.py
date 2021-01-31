# 뷰티풀수프 상용어구, 셀레니움 추가 
import requests, time
from bs4 import BeautifulSoup  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
key = '아이유'
basic = 'https://ko.wikipedia.org'
url = 'https://ko.wikipedia.org/wiki/' + key

def bs(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    return BeautifulSoup(requests.get(url, headers = headers).text,'lxml') 
k = 0
for j in bs(url).find_all('div',{'class':'thumbinner'}):
    url2 = basic + j.find('a').get('href')
    soup2 = bs(url2).find('div',{'class':'fullImageLink'}).find('a').get('href')
    # print(soup2)
    k +=1
    try:
        # upload 할 때 url 주소가 정확한지 확ㅇ니
        soup2 = 'https:' + soup2
        print(soup2)
        # 확장자에 따라서 다르게 표현
        if url2[-3:] =='jpg':
            with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+key + str(k)+'.jpg', 'wb') as f:
                f.write(requests.get(soup2).content)
        else:
            with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+key + str(k)+'.png', 'wb') as f:
                f.write(requests.get(soup2).content)
    except:
        pass

 