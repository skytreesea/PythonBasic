import os 
os.chdir(r'C:\Users\ERC\Documents\GitHub\PythonBasic\csv')
import usecsv
ad=[[1,2,3],['우리','나라','만세'],['나는','우리나라가','좋다']]
usecsv.writecsv('new_write_file.csv',ad)
total = usecsv.opencsv('new.csv')
print(total)