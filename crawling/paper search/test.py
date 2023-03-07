
import json 
with open(r"C:\Users\ERC\Documents\GitHub\PythonBasic\crawling\paper search\web_paper.json", 'r') as file:
    new = json.load(file.encode().decode('unicode_escape'))
    
print(new)