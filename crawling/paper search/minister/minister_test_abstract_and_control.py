# 국회도서관 크롤링: 상세페이지에서 정보 꺼내기
from bs4 import BeautifulSoup
import requests
import re
from warnings import simplefilter
author = '김창현'
controlno_sample = 'KDMT1201106059'

def get_paper_controlno_from_name(name):
    data = []
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    url =  'https://dl.nanet.go.kr/search/searchInnerList.do?refineSearchYn=N&userClass=0&seqNo=0&searchType=INNER_SEARCH&topMainMenuCode=KDMT_ALL&navigationSize=5&nopMenu=REFD&pageSize=100&orderBy=WEIGHT&rspTime=0.528&hanjaYn=Y&pageNum=1&dpBranch=ALL&totalSizeByMenu=30&branchCode=ALL&topSubMenuCode=KDMT_ALL&bestMeterialSearchQuery=+'+name+'%3AALL_NI_TOC%3AAND&totalSize=302&zone=ALL_NI_TOC&searchMehtod=F&searchQuery=+'+name+ '&queryText='+name+'%3AALL_NI_TOC%3AAND&resultType=INNER_SEARCH_LIST&searchClass=S&asideState=true'
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    pattern = r"'([^']*)'"  
    # Loop through all <item> tags  
    for i in soup.find_all('div',{'class':'searchList'}): 
        for j in i.select('a'):
            try: 
                result = re.search(pattern, j.get('href'))
                ret.append(result.group(1))
            except:
                pass
    return ret
    
def get_paper_supervisor_and_abstract_nanet(controlNo):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    url =  'http://dl.nanet.go.kr/search/searchInnerDetail.do?controlNo=' + controlNo
    soup = BeautifulSoup(requests.get(url, verify=False, headers=headers).text, 'lxml')
    #newData={}
    print(soup.find('dl', {'id': 'DETAIL_REMARK'}))

    
    #for i in soup.find_all('div',{'class':'detailContent2'}):
        #for j in i.find_all('p'):
            #print(j.text.strip('\ufeff'))
# https://dl.nanet.go.kr/search/searchInnerDetail.do?controlNo=KDMT1201905905 둘 다 있음 
#for i in get_paper_controlno_from_name('김창현'):
    #get_paper_minister(i) 
    
#for controlno in get_paper_controlno_from_name('권규상'):
    
print(get_paper_supervisor_and_abstract_nanet('KDMT120190590'))
    
 