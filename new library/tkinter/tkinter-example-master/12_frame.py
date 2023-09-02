from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")


Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리모양, bd : 두께
frame_burger.pack(side="left", fill="both", expand=True) # fill : both는 위아래로 꽉꽉 채우는거, expand : 좌우로 펼쳐지는 옵션

Button
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()


frame_drink = LabelFrame(root, text="음료") # 제목이 있는 프레임
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()