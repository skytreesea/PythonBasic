# -*- coding: 牢内爹 -*-
import sys
sys.setdefaultencoding('牢内爹')
import json

# JSON 单捞磐 积己
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# JSON 颇老 积己 棺 单捞磐 历厘
with open("data.json", "w") as outfile:
    json.dump(data, outfile)