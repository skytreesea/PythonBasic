import tkinter as tk

def convert_to_pyung():
    square_meter = float(entry.get())
    pyung = square_meter / 3.3
    result_label.config(text=f"{name}, {num}, {pyung:.2f} 평")

# tkinter 윈도우 생성
window = tk.Tk()
window.title("제곱미터를 평으로 변환")
window.geometry("300x150")

# 레이블과 엔트리 생성
name = tk.Label(window, text="이름:")
name.pack()

label = tk.Entry(window)
label.pack()
# 레이블과 엔트리 생성
num = tk.Label(window, text="가격:")
num.pack()

label = tk.Entry(window)
label.pack()
# 레이블과 엔트리 생성
label = tk.Label(window, text="제곱미터:")
label.pack()

entry = tk.Entry(window)
entry.pack()
# 변환 버튼 생성
convert_button = tk.Button(window, text="변환", command=convert_to_pyung)
convert_button.pack()

# 결과 표시 레이블 생성
result_label = tk.Label(window, text="")
result_label.pack()

# tkinter 이벤트 루프 시작
window.mainloop()