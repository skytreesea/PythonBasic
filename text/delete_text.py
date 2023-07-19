import os

folder_path = r'C:\Users\skytr\Documents\GitHub\PythonBasic\text'  # 폴더 경로를 지정하세요

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        os.unlink(os.path.join(folder_path, file_name))