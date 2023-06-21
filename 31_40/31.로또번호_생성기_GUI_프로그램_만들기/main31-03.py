import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick():
    for i in range(5):
        # 랜덤으로 생성된 번호 6개를 map함수를 사용하여 문자열로 변환
        lottoPick = map(str,random.sample(lotto_num,6))
        
        # 문자열 리스트를 합쳐서 하나의 문자열로 변환.
        lottoPick = ','.join(lottoPick)
        
        lottoPick = str(i+1) + "회: " + lottoPick
        print(lottoPick)
        
        # 리스트 박스에 값을 넣는다.
        listbox.insert(i, lottoPick)
    listbox.pack()
    
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

font = tkinter.font.Font(size = 20)
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)
listbox.insert(0, "1회:")
listbox.insert(1, "2회:")
listbox.insert(2, "3회:")
listbox.insert(3, "4회:")
listbox.insert(4, "5회:")
listbox.pack()

window.mainloop()