# -*- coding: ���ڵ� -*-
import sys
sys.setdefaultencoding('���ڵ�')
import json

# JSON ������ ����
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# JSON ���� ���� �� ������ ����
with open("data.json", "w") as outfile:
    json.dump(data, outfile)