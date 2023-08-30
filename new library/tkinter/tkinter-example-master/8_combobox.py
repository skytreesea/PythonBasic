from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정



readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()