import pandas as pd
import matplotlib.pyplot as plt
import csv, os 
os.chdir(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\raw')
csvs = os.listdir()

def opencsv(filename):
    f=open(filename, 'r', encoding='cp949')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output
	
def writecsv(filename, the_list):
    with open(filename,'w',newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

for i in csvs:
    try:
        total = opencsv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\raw\가공전\\' + i )
        total = total[15:]
        print(total[:5])
        writecsv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장\raw\가공후\\'+i, total )
    except:
        pass