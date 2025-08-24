from tkinter import *
import os

def reset():
    os.system("shutdown /r /t 1")
    
def reset_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
    
def shutdown():
    os.system("shutdown /s /t 1")
    

root=Tk()
root.geometry("500x500")
root.config(bg="blue")

reset_btn=Button(root,text="Restart",font=("Times New Roman",20),command=reset)
reset_btn.place(x=180,y=20,height=50,width=160)

resettime_btn=Button(root,text="Restart Time",font=("Times New Roman",20),command=reset_time)
resettime_btn.place(x=180,y=120)

logout_btn=Button(root,text="Logout",font=("Times New Roman",20),command=logout)
logout_btn.place(x=180,y=240,height=50,width=160)

shutdown_btn=Button(root,text="Shutdown",font=("Times New Roman",20),command=shutdown)
shutdown_btn.place(x=180,y=340,height=50,width=160)

root.mainloop()