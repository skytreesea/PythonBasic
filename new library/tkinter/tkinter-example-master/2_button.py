from tkinter import *

root = Tk()

root.title("Hoon GUI")
btn1 = Button(root, text="버튼1")
btn1.pack() #이거를 해줘야 화면창에 보임


btn2 = Button(root, padx=5, pady=10, text="버튼2")  #padx는 버튼의 넓이, pady는 높낮이 조정. 버튼 내부에서 좌우/상하 공간 확보하는 형태임. 글자가 늘어나면 버튼도 자동으로 늘어남
btn2.pack()


btn3 = Button(root, padx=20, pady=5, text="버튼3")
btn3.pack()


btn4 = Button(root, width=10, height=3, text="버튼4")   #버튼 크기 자체를 설정. 글자가 크기를 넘어가면 짤림
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")   #fg : 글자색깔, bg : 백그라운드
btn5.pack()

photo = PhotoImage(file=r"C:\Users\user\Documents\PythonBasic\new library\tkinter\tkinter-example-master\image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) #command : 함수 동작할 때 사용
btn7.pack()

root.mainloop()