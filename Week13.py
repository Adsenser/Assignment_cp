from tkinter import *
from tkinter.simpledialog import *
window = Tk()

window.title("사칙연산 계산기")
window.geometry("500x300")
window.resizable(width = False, height = False)

def myFunc():
    global symbol
    if var.get() ==1:
        label2.configure(text = "+")
        symbol = 1
    if var.get() ==2:
        label2.configure(text = "-")
        symbol = 2
    if var.get() ==3:
        label2.configure(text = "x")
        symbol = 3
    if var.get() ==4:
        label2.configure(text = "/")
        symbol = 4

def myResult():
    if symbol == 1:
        result = value1 + value2
        label5.configure(text=result)
    elif symbol == 2:
        result = value1 - value2
        label5.configure(text=result)
    elif symbol == 3:
        result = value1 * value2
        label5.configure(text=result)
    elif symbol == 4:
        result = value1 / value2
        label5.configure(text=result)

def inputnum1():
    global value1
    value1 = askinteger("숫자 입력","첫번째 숫자를 입력하세요(0~100)",minvalue=0,maxvalue=100)
    label1.configure(text=value1)

def inputnum2():
    global value2
    value2 = askinteger("숫자 입력","두번째 숫자를 입력하세요(0~100)",minvalue=0,maxvalue=100)
    label3.configure(text=value2)

def out():
    window.quit()
    window.destroy()

#라디오
var = IntVar()
rb1 = Radiobutton(window,text="더하기",variable=var,value=1,command = myFunc)
rb2 = Radiobutton(window,text="빼기",variable=var,value=2,command = myFunc)
rb3 = Radiobutton(window,text="곱하기",variable=var,value=3,command = myFunc)
rb4 = Radiobutton(window,text="나누기",variable=var,value=4,command = myFunc)

#버튼 생성
button1 = Button(window, text = "입력1",command = inputnum1)
button2 = Button(window, text = "입력2",command = inputnum2)
button3 = Button(window, text = "계산",command = myResult)

#종료버튼 생성
button4 = Button(window, text = "Quit",fg="red", command=out)

#결과창 선언
label1 = Label(window,text = "__")
label2 = Label(window,fg="blue",text = "__")
label3 = Label(window,text = "__")
label4 = Label(window,text = "=")
label5 = Label(window,text = "__")

#모양 출력
rb1.place(x = 100,y= 30)
rb2.place(x = 200,y= 30)
rb3.place(x = 300,y= 30)
rb4.place(x = 400,y= 30)

button1.place(x = 150,y= 100)
button2.place(x = 250,y= 100)
button3.place(x = 350,y= 100)

label1.place(x = 100, y=200)
label2.place(x = 150, y=200)
label3.place(x = 200, y=200)
label4.place(x = 250, y=200)
label5.place(x = 300, y=200)

button4.place(x=250,y=270)

window.mainloop()
