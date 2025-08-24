from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()

    hr=time.strftime('%I')
    min=time.strftime("%M")
    sec=time.strftime("%S")
    ap=time.strftime("%p")

    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ap.config(text=ap)

    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)


    lab_hr.after(200,date_time)




root=Tk()
root.title("Digital Clock")
root.geometry("860x340")
root.config(bg="#7A85C1")

lab_hr=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_hr.place(x=40,y=40,height=100,width=100)
lab_hr_txt=Label(root,text="Hour",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_hr_txt.place(x=140,y=100,height=40,width=80)

lab_min=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_min.place(x=240,y=40,height=100,width=100)
lab_min_txt=Label(root,text="Min",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_min_txt.place(x=340,y=100,height=40,width=80)

lab_sec=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_sec.place(x=440,y=40,height=100,width=100)
lab_sec_txt=Label(root,text="Sec",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_sec_txt.place(x=540,y=100,height=40,width=80)

lab_ap=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_ap.place(x=640,y=40,height=100,width=100)
lab_ap_txt=Label(root,text="AM/PM",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_ap_txt.place(x=745,y=100,height=40,width=80)


lab_date=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_date.place(x=40,y=180,height=100,width=100)
lab_date_txt=Label(root,text="Date",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_date_txt.place(x=140,y=240,height=40,width=80)

lab_mon=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_mon.place(x=240,y=180,height=100,width=100)
lab_mon_txt=Label(root,text="Month",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_mon_txt.place(x=340,y=240,height=40,width=80)

lab_year=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_year.place(x=440,y=180,height=100,width=100)
lab_year_txt=Label(root,text="Year",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_year_txt.place(x=540,y=240,height=40,width=80)

lab_day=Label(root,text="00",font=("",30,"bold"),bg="#1A2A80",fg="white")
lab_day.place(x=640,y=180,height=100,width=100)
lab_day_txt=Label(root,text="DAY",font=("",15,"bold"),bg="#7A85C1",fg="white")
lab_day_txt.place(x=745,y=240,height=40,width=80)

date_time()

root.mainloop()