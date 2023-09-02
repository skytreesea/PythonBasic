from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # 스크롤 바 오른쪽으로, fill=y : y방향으로 꽉채우는거


# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set) # yscrollcommand : y축으로 스크롤 넣는 기능

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")

#listbox랑 스크롤 박스가 서로 바라보게 해야함
scrollbar.config(command=listbox.yview)

root.mainloop()