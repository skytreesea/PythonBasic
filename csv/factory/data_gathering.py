import pandas as pd
import matplotlib.pyplot as plt
import csv, os 
# CSV 파일이 저장된 디렉토리 경로
dir_path = r"C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장장_프로젝트_2023\raw\의뢰\all"

# 해당 디렉토리에 있는 모든 파일의 이름을 가져옵니다.
file_names = os.listdir(dir_path)

# 빈 DataFrame 생성
merged_df = pd.DataFrame()

# 각 파일을 읽어서 DataFrame에 추가합니다.
for file_name in file_names:
    if file_name.endswith('.csv'):  # CSV 파일만 처리
        file_path = os.path.join(dir_path, file_name)
        temp_df = pd.read_csv(file_path)
        
        # 각 파일의 DataFrame을 병합
        merged_df = pd.concat([merged_df, temp_df])

# 결과 DataFrame 확인
merged_df.to_csv(r'C:\Users\skytr\OneDrive\문서\김창현\긱스퍼트\공장장_프로젝트_2023\raw\merged_v2.csv', encoding = 'utf-8-sig')
