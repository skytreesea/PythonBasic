from tkinter import *

root = Tk()


root.title("Hoon GUI")
#root.geometry("640x480") #가로 * 세로
root.geometry("640x480+800+300") #가로x세로 + x좌표 + y좌표   -> 컴퓨터 맨 왼쪽 기준으로 창 나오는 위치 설정 가능
root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()