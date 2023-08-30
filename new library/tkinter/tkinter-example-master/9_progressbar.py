from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate : 결정되지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate : 결정되지 않음
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 1.5% 이런식으로 올라갈 수 있어서 실수 반영.
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # 동작할 때 매번 gui에 반영해줘야함
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()