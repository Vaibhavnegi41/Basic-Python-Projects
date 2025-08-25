from tkinter import *

data=""

def get_data(value):
    global data
    data=data + str(value)
    var.set(data)

def clear():
    global data
    data=""
    var.set(data)

def equal():
    global data
    try:
        total=str(eval(data))
        var.set(total)
        data=""
    except :
        var.set("Error")

root=Tk()
root.geometry("400x600")
root.resizable(False,False)
root.config(bg="#93DA97")

var=StringVar()

lab=Label(root,text="Calculator",font=("Franklin Gothic Heavy",30),bg="#93DA97")
lab.pack(pady=10)

entry=Entry(root,textvariable=var,font=("",20,"bold"))
entry.place(x=60,y=70,height=50,width=288)

# ---------------for first row--------------
btn1=Button(root,text="1",font=("Franklin Gothic Heavy",20),command=lambda:get_data(1))
btn1.place(x=60,y=160,height=60,width=70)

btn2=Button(root,text="2",font=("Franklin Gothic Heavy",20),command=lambda:get_data(2))
btn2.place(x=135,y=160,height=60,width=70)

btn3=Button(root,text="3",font=("Franklin Gothic Heavy",20),command=lambda:get_data(3))
btn3.place(x=210,y=160,height=60,width=70)

btn_add=Button(root,text="+",font=(20),command=lambda:get_data("+"))
btn_add.place(x=285,y=160,height=60,width=70)

# ------------for second row-------------------
btn4=Button(root,text="4",font=("Franklin Gothic Heavy",20),command=lambda:get_data(4))
btn4.place(x=60,y=240,height=60,width=70)

btn5=Button(root,text="5",font=("Franklin Gothic Heavy",20),command=lambda:get_data(5))
btn5.place(x=135,y=240,height=60,width=70)

btn6=Button(root,text="6",font=("Franklin Gothic Heavy",20),command=lambda:get_data(6))
btn6.place(x=210,y=240,height=60,width=70)

btn_sub=Button(root,text="-",font=(20),command=lambda:get_data("-"))
btn_sub.place(x=285,y=240,height=60,width=70)

# ---------for third row---------------------
btn7=Button(root,text="7",font=("Franklin Gothic Heavy",20),command=lambda:get_data(7))
btn7.place(x=60,y=320,height=60,width=70)

btn8=Button(root,text="8",font=("Franklin Gothic Heavy",20),command=lambda:get_data(8))
btn8.place(x=135,y=320,height=60,width=70)

btn9=Button(root,text="9",font=("Franklin Gothic Heavy",20),command=lambda:get_data(9))
btn9.place(x=210,y=320,height=60,width=70)

btn_mul=Button(root,text="x",font=(20),command=lambda:get_data("*"))
btn_mul.place(x=285,y=320,height=60,width=70)

# ---------for fourth row--------------------
btn0=Button(root,text="0",font=("Franklin Gothic Heavy",20),command=lambda:get_data(0))
btn0.place(x=60,y=400,height=60,width=70)

btnc=Button(root,text="Clear",font=("Franklin Gothic Heavy",15),command=clear)
btnc.place(x=135,y=400,height=60,width=70)

btn_dot=Button(root,text=".",font=(30),command=lambda:get_data("."))
btn_dot.place(x=210,y=400,height=60,width=70)

btn_div=Button(root,text="/",font=(20),command=lambda:get_data("/"))
btn_div.place(x=285,y=400,height=60,width=70)

# -----------------for fifth row------------------
btn_equal=Button(root,text="=",font=(30),command=equal,bg="#5E936C",fg="white")
btn_equal.place(x=135,y=480,height=60,width=145)

root.mainloop()