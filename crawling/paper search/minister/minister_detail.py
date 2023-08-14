import requests

url = 'https://openapi.nanet.go.kr/nadl/rest/detailinfoservice/detail'
params ={'serviceKey' : '7JlKxM7fEbOErQRa32MtR3/g/Bxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK+w7YSwijxr0Tklej3cOg==', 'controlno' : 'MONO1201027232' }

response = requests.get(url, params=params)
print(response.content)