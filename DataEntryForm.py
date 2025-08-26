from tkinter import *
from tkinter.messagebox import showinfo,showerror,showwarning
import sqlite3 as sq


def init_db():
    connection=sq.connect("entry_data.db")
    cursor=connection.cursor()

    cursor.execute('''
        
        CREATE TABLE IF NOT EXISTS userInfo(
                
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                title TEXT,
                age INT NOT NULL,
                nationality TEXT,
                courses INT,
                semester INT,
                registered TEXT
                )

    ''')
    connection.commit()
    connection.close()

def upload_data(fname,lname,title,age,nationality,courses,semester,registered):
    connection=sq.connect("entry_data.db")
    cursor=connection.cursor()
    cursor.execute("INSERT INTO userInfo (fname,lname,title,age,nationality,courses,semester,registered) VALUES (?,?,?,?,?,?,?,?)",
                   (fname,lname,title,age,nationality,courses,semester,registered))
    connection.commit()
    connection.close()

def list_all_records():
    connection=sq.connect("entry_data.db")
    cursor=connection.cursor()
    data=cursor.execute("SELECT * FROM userInfo")
    records=data.fetchall()
    connection.close()

    for row in records:
        print("\n")
        print("*"*130)
        print(f"First Name :{row[0]} | Last Name :{row[1]} | Title :{row[2]}")
        print(f"Age :{row[3]} | Nationality :{row[4]}")
        print(f"Courses :{row[5]} | Semester :{row[6]}")

        if row[7] :
            print(f"Registration Status : Done")
        else:
            print(f"Registration Status : Not completed")

        print("*"*130)
        print("\n")


root=Tk()
root.title("Registration Form")
root.geometry("650x500")

def verify():

    if accept.get() and registered.get() :

        if fname.get() != "" and lname.get() !="" :

            upload_data(fname.get(),lname.get(),title.get(),age.get(),nationality.get(),courses.get(),semesters.get(),registered.get())

            list_all_records()

            showinfo(
                title="Verify",
                message="You Successfully registered yourself !"
            )

            root.destroy()

        else:
            showerror(
                title="Error Found",
                message="Please enter complete details related to name."
            )

    else:

        showwarning(
            title="Warning",
            message="Please confirm the terms and conditions !"
        )



fname=StringVar()
lname=StringVar()
title=StringVar()
age=IntVar()
nationality=StringVar()
registered=IntVar()
courses=IntVar()
semesters=IntVar()
accept=IntVar()



# --------first block------------------------------
lf1=LabelFrame(root,text="User Information")
lf1.place(x=20,y=20,height=200,width=600)

l1=Label(root,text="First Name",font=("",10,"bold"))
l1.place(x=70,y=60)

l2=Label(root,text="Last Name",font=("",10,"bold"))
l2.place(x=260,y=60)


l3=Label(root,text="Title",font=("",10,"bold"))
l3.place(x=420,y=60)

e1=Entry(root,textvariable=fname)
e1.place(x=50,y=100)

e2=Entry(root,textvariable=lname)
e2.place(x=240,y=100)

options=["Mr","Mrs"]
sp1=Spinbox(root,value=options,font=("",10,"bold"),wrap=True,textvariable=title)
sp1.place(x=420,y=100)

l4=Label(root,text="Age",font=("",10,"bold"))
l4.place(x=90,y=140)
sp2=Spinbox(root,from_=1,to=120,wrap=True,textvariable=age)
sp2.place(x=50,y=170)

l5=Label(root,text="Nationality",font=("",10,"bold"))
l5.place(x=260,y=140)
nations=["India","Sri Lanka","Australia","Russia","USA","Germany","Poland","Greece","Japan","Singapore","South Korea"]
sp3=Spinbox(root,value=nations,wrap=True,textvariable=nationality)
sp3.place(x=240,y=170)

# -------------------second block------------------------------


lf2=LabelFrame(root)
lf2.place(x=20,y=240,height=100,width=600)

l6=Label(root,text="Registration Status",font=("",10,"bold"))
l6.place(x=50,y=260)
ch=Checkbutton(root,text="Currently Registeted",font=("",10),variable=registered,onvalue=1,offvalue=0)
ch.place(x=40,y=300)

l7=Label(root,text="Completed Course",font=("",10,"bold"))
l7.place(x=250,y=260)
sp4=Spinbox(root,from_=1,to=40,wrap=True,textvariable=courses)
sp4.place(x=240,y=300)

l8=Label(root,text="Semesters",font=("",10,"bold"))
l8.place(x=450,y=260)
sp5=Spinbox(root,from_=1,to=8,wrap=True,textvariable=semesters)
sp5.place(x=440,y=300)

# -----------------third block-------------------------------

lf3=LabelFrame(root,text="Terms & Conditions")
lf3.place(x=20,y=350,height=80,width=600)

ch2=Checkbutton(root,text="I accept the terms and conditions.",font=("",10),variable=accept,onvalue=1,offvalue=0)
ch2.place(x=40,y=380)


# --------------------enter button-----------------------------

btn=Button(root,text="Enter Data",font=("",15,"bold"),command=verify)
btn.place(x=20,y=440,height=40,width=600)



init_db()
root.mainloop()