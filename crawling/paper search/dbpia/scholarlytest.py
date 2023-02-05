# 영문으로는 뭔가 검색하는데 성공 which can't search Korean authors 
# not completed
import json
from scholarly import scholarly
keyword = "harvey" 
# will paginate to the next page by default
authors = scholarly.search_author(keyword)
a= 0
for author in authors:
    if a < 4:
        print(json.dumps(author, indent=2))
    else: break
    a += 1