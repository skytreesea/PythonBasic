import os 
import pandas as pd

from requests import get  
url = "https://www.mois.go.kr/cmm/fms/FileDown.do?atchFileId=FILE_00097363HTVwgCo&fileSn=0"
#특정 주소로 가서 파일을 현재 폴더 다운받는 매서드
file_path = os.getcwd()+'\public_firms.xls'
with open(file_path, "wb") as file:   
    response = get(url)               
    file.write(response.content)      

df = pd.read_excel(file_path)
# 윗 두 줄은 불필요하니 잘라내는 
df = df.iloc[2:,:]
# 잘라내고 남은 첫 행이 칼럼명이 됨
df.columns = df.iloc[0]
to_firms=pd.crosstab(df['지역'],df['공기업유형'])
to_firms.to_clipboard()
