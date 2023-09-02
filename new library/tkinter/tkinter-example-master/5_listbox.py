from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=3)    # selectmode : single은 1개만 선택 가능. extended는 여러개 선택 가능. 
                                                            # height 0일 떄는 리스트 다 보여주고, 3이면 3개만 보여줌. 키보드로 내려야함
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") #END : 리스트박스 마지막에 넣어줌
listbox.insert(END, "포도")

listbox.pack()

def btncmd():
    #listbox.delete(END) # 맨 뒤에 항목을 삭제
    
    #개수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된 항목
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()