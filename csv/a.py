import os
os.chdir(r'C:\Users\ERC\Documents\GitHub\PythonBasic\basic_test')

f= open('new_and_new.txt','w',encoding='utf-8')
f.write('나는 배가 고픕니다. 나는 밥을 먹고 싶습니다.')
f.close()
print(os.listdir())
 