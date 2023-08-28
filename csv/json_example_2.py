import json

# JSON 데이터 생성
data = {
    "지자체": "광주남구",
    "공무원": '30',
    "기간제": '20'
}

# JSON 파일 생성 및 데이터 저장
with open(r"C:\Users\ERC\Documents\GitHub\PythonBasic\csv\\data.json", "w") as outfile:
    json.dump(data, outfile)
    
  # JSON에서 값 찾기    
with open(r"C:\Users\ERC\Documents\GitHub\PythonBasic\csv\\data.json", "r") as infile:
    dataset = json.load(infile)
    
def load_and_print(data):
    result =  ('안녕하세요{} 주민여러분, 공무원 수는 {}명이에요. 기간제는 {}명입니다.'.format(data['지자체'], data["공무원"],data["기간제"] ))
    return result
    
print(load_and_print(dataset))