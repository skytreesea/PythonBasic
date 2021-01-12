import os

os.chdir(r'C:\Users\ERC\Documents\GitHub\do-it-python\05\feasibility\data')
print(os.listdir())

f = open('a.txt','r',encoding='utf-8')
print(f.readlines())
f.close()
