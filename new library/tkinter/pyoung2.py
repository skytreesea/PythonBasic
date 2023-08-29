import tkinter as tk
from tkinter import messagebox

def convert_to_pyung():
    try:
        square_meters = float(entry.get())
        pyung = square_meters / 3.3
        result_label.config(text=f"{square_meters:.2f} 제곱미터 = {pyung:.2f} 평")
    except ValueError:
        messagebox.showerror("에러", "유효한 숫자를 입력해주세요.")

# 메인 윈도우 생성
root = tk.Tk()
root.title("제곱미터를 평으로 변환")

# 라벨 및 엔트리 위젯 생성
label = tk.Label(root, text="제곱미터를 입력하세요:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="변환", command=convert_to_pyung)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Malgun Gothic", 14))
result_label.pack(pady=10)

# 메인 루프 실행
root.mainloop()