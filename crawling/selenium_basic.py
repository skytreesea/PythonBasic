# 셀레니움 접근법 기본명령
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'"D:\user\Documents\chromedriver.exe"')
driver.get('https://www.naver.com')