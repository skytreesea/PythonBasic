import usecsv, os 
# 경로이동
os.chdir(r'D:\user\Documents\git hub\PythonBasic\csv')
# csv 형 파일 생성
test_csv = [['국어', '영어','수학'], [90,80,100]]
# 쓰기: usecsv.writecsv(파일명, 리스트명)
usecsv.writecsv('making_csv.csv', test_csv)
# 읽기: usecsv.opencsv(파일명)  -->  보통 특정객체로 저장해서 사용 
new = usecsv.opencsv('making_csv.csv')
print(new)
