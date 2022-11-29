from tkinter import *
from tkinter.simpledialog import *

def operator():
    if var.get() == 1:
        label1.configure(text = "+")
    elif var.get() == 2:
        label1.configure(text="-")
    elif var.get() == 3:
        label1.configure(text="*")
    elif var.get() == 4:
        label1.configure(text="/")

value2 = 0
value3 = 0

def input1():
    global value2
    value2 = askinteger("숫자입력","숫자 입력1 (1~100)",minvalue=0,maxvalue=100)
    label2.configure(text =str(value2))

def input2():
    global value3
    value3 = askinteger("숫자입력","숫자 입력2 (1~100)",minvalue=0,maxvalue=100)
    label3.configure(text =str(value3))

def calc():
    if var.get() == 1:
        result = value2 + value3
    elif var.get() == 2:
        result = value2 - value3
    elif var.get() == 3:
        result = value2 * value3
    elif var.get() == 4:
        result = value2 / value3
    label5.configure(text=result)

def func_exit():
    window.quit()
    window.destroy()

window = Tk()

window.title("사칙연산 계산기")
window.geometry("400x200")
window.resizable(width =False, height = False)

var = IntVar()
rb1 = Radiobutton(window, text="더하기",variable = var,value =1, command=operator)
rb2 = Radiobutton(window, text="빼기",variable = var,value =2, command=operator)
rb3 = Radiobutton(window, text="곱하기",variable = var,value =3, command=operator)
rb4 = Radiobutton(window, text="나누기",variable = var,value =4, command=operator)

rb1.place(x=20,y=30)
rb2.place(x=120,y=30)
rb3.place(x=220,y=30)
rb4.place(x=320,y=30)

label1 = Label(window, text="__")
label2 = Label(window, text="__")
label3 = Label(window, text="__")
label4 = Label(window, text="=")
label5 = Label(window, text="__")
label1.place(x=150,y=130)
label2.place(x=120,y=130)
label3.place(x=180,y=130)
label4.place(x=210,y=130)
label5.place(x=230,y=130)

btn2 = Button(window,text = "입력1" , command = input1)
btn2.place(x=100,y=75)
btn3 = Button(window,text = "입력2" , command = input2)
btn3.place(x=200,y=75)
btn4 = Button(window,text = "계산" , command = calc)
btn4.place(x=300,y=75)

button1 = Button(window,text = "Quit",command=func_exit)
button1.place(x=200,y=180)

window.mainloop()
