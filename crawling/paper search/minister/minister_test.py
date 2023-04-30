# 국회도서관 크롤링 1차 성공
from bs4 import BeautifulSoup
import requests
import re
author = '윤세찬'

# 두 리스트가 있을 때 이것을 dataset으로 만들어주는 코드 필요
def make_list_to_dict(list1, list2):
    result = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            result[list1[i]] = list2[i]
    return result

# 태그가 있다면 없애주는 함수
def remove_tags(html):
    # Remove HTML tags using regular expressions
    clean_text = re.sub('<.*?>', '', html)

    return clean_text

def get_paper_minister(name):
    data = []
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    url = 'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageno=1&displaylines=100&search=저자,' + name
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    # Loop through all <item> tags
    try:
        for recode in soup.find_all('recode'):
            #print(recode)
            for i in recode.find_all('item'):
                if i.find('name').text == '지도교수':
                    newData= make_list_to_dict(       [i.text for i in recode.find_all('name')],
                        [remove_tags(i.text) for i in recode.find_all('value')])
                    print(newData)
                    print(newData['제어번호'])
               #     newData = make_list_to_dict(
                #        [i.text for i in recode.find_all('name')],
                #        [remove_tags(i.text) for i in recode.find_all('value')]
                  #  )
                         
                    #title=newData['지도교수']
                        #author=newData['지도교수'],
                        #university=newData['지도교수'],
                        #norm_university=newData['지도교수'],
                        #year=newData['지도교수'],
                        #gubun=newData['지도교수'],  # 박사/석사 구분 HTML 추가 필요
                        #link=newData['지도교수']
                    
                    #success += 1
                    #data.append(newData)
    except:
        print('Grieve.')
    return data

print(get_paper_minister(author))