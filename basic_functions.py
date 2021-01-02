# 2강 basic 5 강의
# 파이썬의 변수의 유형 초 간단 정리: int, str, float, list, dict
# 파이썬 초심자를 위한 기초 함수: 
# 1. 출력: print
# 2. 반복: for
# 3. 조건문: if
# 4. 함수지정: def  

#출력하기 
print("Hello, world")

#포매팅으로 출렷하기
print('Hello, world! I am %d years old. My name is %s.'%(33, 'Changhyun'))
age = 36
print('I am %d years old' % age)
# 포매팅 원리 
print('I am {age} years old and live in {city}'.format(age = 4, city = 'Seoul'))

# 유형의 기본만 알아봅시다. 
# 정수 
print(type(3))
# 부동소수 float
print(type(3.5))
# 문자 str
print(type('나는 문자열입니다. string이라고 하고 파이썬에서는 str이라고 합니다.'))
# 리스트 list
print(type([2,3,3]))
potal ={'naver':'네이버','daum':'다음','yahoo':'야후'}
print(type(potal))
print(potal['naver'])
print(potal.keys())
print(potal.values())

# 문자와 숫자 결합 X, 결합이 같아야 합칠 수 있음
print(2+3)
print("I", " and you are friends.")
print(3+5)
print("저는 "+str(34)+ "살입니다.")
# 오류 사례예문 print("저는 "+34+ "살입니다.")

# 리스트형
newlist = ["서울","부산","대구","대전"]
print(newlist)
print(len(newlist))
# 추가
newlist.append('광주')
print(newlist)
# 리스트 인덱싱(indexing), 슬라이싱(슬라이싱)
print(newlist[0])
print(newlist[4])
print(newlist.insert(4,"울산"))
print(newlist)
# 서울의 인덱스는? 
print(newlist.index('서울'))
# 슬라이싱, 첫 원소만 빼고 두번째부터 출력하기
print(newlist[1:])
# 반복문 for
for i in newlist:
    print(i)
    print("내 고향은",i,"입니다.")
    print("내 고향은 %s입니다."%i)

# 조건문 '대'로 시작하는 
for i in newlist:
    if i[0] =='대':
        print("대로 시작하는 도시는 %s입니다." %i)
# 조건문 '대'로 시작하지 않는 조건
for i in newlist:
    if i[0] =='대':
        print("대로 시작하는 도시는 %s입니다" %i)
    elif i[-1] =='산':
        print('산으로 끝나는 도시는 %s입니다'%i)
    else:
        print('%s는 모두 해당되지 않습니다.'%i)

# range 함수 
for i in range(10):
    print(i)
# 구구단 만들기 j단, 곱해지는 수 i 
for i in range(1,10):
    for j in range(2,10):
        print('%d X %d = %d' %(j, i, i*j))

# len 함수와 결합하여, 모든 리스트 내용물 출력, 리스트 몇 개 요소 있는지 모름
for i in range(len(newlist)):
    print(newlist[i])
# 리스트 안에 리스트가 있는 경우
new_complex_list = [[1,2,3],["우리","나라","만세"]]
print(new_complex_list)
# 리스트 안에 리스트가 있는 경우

# 리스트 안에 리스트가 있는 경우
new_complex_list = [[1,2,3],["우리","나라","만세"]]
for i in new_complex_list:
    print(i)
#나라만 찍어서 출력하고 싶어요
print(new_complex_list[1][1])
#2와 나라만 출력
for i in new_complex_list:
    print(i[1])
# 조금은 긴 데이터
data_complex = [["우리","나라","만세"],[23,33,34],[53,53,74],[73,63,55],[83,63,44]]
# 조금은 긴 데이터 앞 부분만 보기
for i in data_complex[:3]:
    print(i)
# 만세 부분만 출력
for i in data_complex:
    print(i[-1]) 

# 데이터를 입력받아서 그 구구단 출력
def gugu(number):
    print(str(number)+"단 구구단을 출력합니다.\n")
    for i in range(1,10):
        print('%d x %d = %d' %(number, i, number*i))
# gugu 함수 실행
gugu(5)

# (중요) return과 print의 차이: 반환하다 개념
#숫자로 된 리스트를 입력받아 평균을 출력함
def average(int_list):
    k=0
    for i in int_list:
        k = k + i
    print(k/len(int_list))

the_list = [4,5,6,7,8,9]
average(the_list)

# return으로 반환하게 함
def average(int_list):
    k=0
    for i in int_list:
        k = k + i
    return k/len(int_list)
# return 받은 값이 표현되지 않아 아무 일 일어나지 않은 것처럼 보입니다. 
average(the_list)

# 그러나 출력된 값으로는 계산할 수 없지만, return 값으로는 계산할 수 있습니다.
print(average(the_list)+ 500)

import os 
print(os.listdir())
os.chdir(r'D:\user\Documents\git hub\PythonBasic')
f= open('make_a_new_file.txt',"w",encoding='utf-8')
f.write('나는 새로운 파일을 만들었습니다.')
f.close()
