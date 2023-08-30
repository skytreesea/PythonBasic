from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480") 

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file=r"C:\Users\user\Documents\PythonBasic\new library\tkinter\tkinter-example-master\image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") #config를 사용해서 안에 내용을 바꿀 수 있음

    global photo2   #가비지 컬렉터가 회수해버림. 전역변수로 만들어야 안죽는다.
    photo2 = PhotoImage(file=r"C:\Users\user\Documents\PythonBasic\new library\tkinter\tkinter-example-master\image2.png")
    label2.config(image=photo2) 

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()