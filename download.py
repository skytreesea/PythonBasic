from requests import get  
def download(url, file_name = None):
	if not file_name:
		file_name = url.split('/')[-1]

	with open(file_name, "wb") as file:   
        	response = get(url)               
        	file.write(response.content)      

if __name__ == '__main__':
	url = "https://image.yes24.com/Goods/5876905/L"
	download(url)