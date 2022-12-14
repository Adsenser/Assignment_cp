from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter import messagebox
import pandas as pd

window = Tk()

window.title("성적 처리 프로그램")
window.geometry("500x300")
window.resizable(width = False, height = False)

mainMenu = Menu(window)
window.config(menu = mainMenu)

#메인 코드 부분1
label1 = Label(window,text = "선택된 파일")
label1.pack()
#메인 코드 부분2
def func_open():
    global filename
    filename = askopenfilename(parent=window,filetypes = (("txt 파일", "*.txt"),("모든 파일","*.*")))
    with open(filename, 'r', encoding='UTF-8') as inFp:
        inStr = inFp.readlines()
        label1.configure(text=inStr)
def func_sum():
    with open(filename, 'r', encoding='UTF-8') as inFp:
        inList = inFp.readlines()
        global sum
        sum = []
        for i in range(1, 11):
            a = inList[i]
            b = a.split()
            temp_sum = int(b[2]) + int(b[3]) + int(b[4])
            sum.append(temp_sum)
    messagebox.showinfo("계산완료","총점 계산이 완료되었습니다")
def func_rank():
    with open(filename, 'r', encoding='UTF-8') as inFp:
        inList = inFp.readlines()
        df = pd.DataFrame(
            {'sum': sum}
        )
        a = df['sum'].rank(method='min', ascending=False)
        global rank
        rank = []
        for m in range(len(sum)):
            rank.append(int(a[m]))
    messagebox.showinfo("계산완료", "석차 계산이 완료되었습니다")

def print_result():
    with open(filename, 'r', encoding='UTF-8') as inFp:
        inList = inFp.readlines()
        real2_line = []
        for i in range(1, 11):
            real_line = []
            temp_line = []
            for j in range(0, 5):
                a = inList[i]
                b = a.split()
                temp_line.append(b[j])
            real_line.extend(temp_line)
            real_line.append(sum[i - 1])
            real_line.append(rank[i - 1])
            real2_line.append(real_line)

def out():
    window.quit()
    window.destroy()

#파일 탭 부분
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일",menu = fileMenu)
fileMenu.add_command(label="열기",command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=out)
#성적 탭 부분
scoreMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "성적",menu = scoreMenu)
scoreMenu.add_command(label="총점 계산",command = func_sum)
scoreMenu.add_separator()
scoreMenu.add_command(label="석차 계산",command = func_rank)
scoreMenu.add_separator()
scoreMenu.add_command(label="성적 출력",command = print_result)



window.mainloop()
