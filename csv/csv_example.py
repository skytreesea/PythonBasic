import csv, usecsv, os
csv_test = [['국어', '영어','수학'], [90,80,100]]
os.chdir(r'C:\Users\skytr\Documents\GitHub\PythonBasic\csv')
usecsv.writecsv('score3.csv',csv_test)
