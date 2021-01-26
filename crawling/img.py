# 뷰티풀수프 상용어구, 셀레니움 추가 
from bs4 import BeautifulSoup  
import requests, time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%9E%90%EC%9C%A0%EC%9D%98%EC%97%AC%EC%8B%A0%EC%83%81'
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\GitHub\fast_campus\selenium\chromedriver.exe')
driver.get(url)

def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')       
# 각 단계별로 제대로 작동하는지 살펴본다.  
time.sleep(3)
soup = bs(url)
print(soup.find_all('div',{'class':'_contentRoot image_wrap'}))