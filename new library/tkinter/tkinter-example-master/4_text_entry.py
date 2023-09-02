from tkinter import *

root = Tk()

root.title("Hoon GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5) #여러줄 입력 때 사용
txt.pack()
txt.insert(END, "글자를 입력하세요") #END : 글자 들어갈 INDEX. 기본값 세팅 예제


e = Entry(root, width=30)   #엔터를 입력할 수 없음. 한줄짜리
e.pack()
e.insert(0, "한 줄만 입력해요") #0번째 인덱스에 넣는다

def btncmd():
    print(txt.get("1.0", END)) #처음부터 끝까지 내용 가져와라. 1은 라인1부터 가져와라, 0은 컬럼위치로 0번쨰 위치부터 가져와라

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()