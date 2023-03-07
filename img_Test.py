from PIL import Image
# 이미지 흑백 변경
image = Image.open(r'C:\Users\ERC\Documents\GitHub\PythonBasic\image.jpg')

image = image.convert('L')

image.rotate(45).show()