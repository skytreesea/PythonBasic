import csv, usecsv, os
csv_test = [['국어', '영어','수학'], [90,80,100]]
os.chdir(r'D:\user\Documents\git hub\PythonBasic\csv')
usecsv.writecsv('score.csv',csv_test)
