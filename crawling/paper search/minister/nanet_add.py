test_code = ['KDMT1190000002','KDMT1190000004']

import json, usecsv, datetime

# JSON 파일 경로
json_file_path = r'C:\Users\skytr\Downloads\2020-02-026.한영번역(사회과학)_sample\1113_social_test_set_151317.json'

en_path= r'C:\Users\skytr\Documents\GitHub\GInsight\db\csv\social\test.txt'
# JSON 파일 열기
k=0
with open(en_path, 'w', encoding= 'utf-8') as eof:
    with open(json_file_path, encoding= 'utf-8') as json_file:
        # JSON 데이터 읽기
        data = json.load(json_file)
        for i in data['data'][0:5]:
            #kof.write(i['ko_original']+'\n')
            try:
                eof.write(i['ko']+'\t'+i['en']+'\t'+i['license']+'\t'+i['source']+'\t'+str(datetime.datetime.now())+'\t'+str(datetime.datetime.now())+'\n')
            except:
                print(i)
    