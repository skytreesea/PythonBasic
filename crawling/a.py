x=1
y = 1
if x is not y:
    print('different')
else:
    print('same')

import re
text = '010-232-2323, 02-3323-2223, 011-5252-1535 전화번호 lili@epan.com, skytree@korea.kr'
print(re.findall('\d*-\d*-\d*',text))
print(re.findall('[a-z]*@[a-z\.]*',text))