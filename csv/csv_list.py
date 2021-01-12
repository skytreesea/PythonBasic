list_in_list = [
    ['사람','나무','바다'],
    [2,3,4]
    ]

print(list_in_list)
import csv, os
os.chdir(r'C:\Users\ERC\Documents\GitHub\PythonBasic\csv')
f = open('new.csv','w', newline = '')
new = csv.writer(f)
new.writerows(list_in_list)    
f.close()

f = open('save_info.csv','r')
output = []
new = csv.reader(f)
for i in new:
    output.append(i)
f.close()

print(output)


