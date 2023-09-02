import pandas as pd
import csv
file_name = r'C:\Users\skytr\Downloads\아파트(매매)__실거래가_20230902095632.csv'   # r을 포함해서 입력

with open(file_name, encoding ='cp949') as f:
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
 
def writecsv(file_name2, the_list):
    with open(file_name2,'w',newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)
        
writecsv(file_name, output)