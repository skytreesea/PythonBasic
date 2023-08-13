# 국회도서관 크롤링 1차 성공
from bs4 import BeautifulSoup  
import requests 
import re

Name = "김종원"
def soupMaker(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, 'lxml') 
    
url = 'https://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&displaylines=200&search=저자,'+Name 

soup = soupMaker(url) 

try:
    # Find all 'recode' elements and iterate over them
    for recode in soup.find_all('recode'):
        # Get the text content of each 'recode' element
        recode_text = recode.get_text()
        if 'KDMT' in recode_text:
        # Attempt to decode and print the content without problematic characters
            result = recode_text.encode('utf-8', errors='ignore').decode('utf-8')
            print(result)

            
except UnicodeEncodeError:
    print("UnicodeEncodeError occurred, but it's handled.")