from tkinter import *
import speedtest 

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()

    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"

    lab_down.config(text=down)
    lab_up.config(text=up)


root=Tk()
root.title("Internet Speed Test")
root.geometry("500x550")
root.config(bg="blue")

lab1=Label(root,text="Internet Speed Test",font=("Bodoni MT Black",30,"bold"),bg="blue",fg="red")
lab1.place(x=60,y=40,height=50,width=380)

lab1=Label(root,text="Download Speed",font=("Bahnschrift Condensed",30,"bold"),bg="blue",fg="white")
lab1.place(x=60,y=130,height=50,width=380)

lab_down=Label(root,text="00",font=("Bahnschrift Condensed",30,"bold"),bg="blue",fg="white")
lab_down.place(x=60,y=200,height=50,width=380)

lab1=Label(root,text="Upload Speed",font=("Bahnschrift Condensed",30,"bold"),bg="blue",fg="white")
lab1.place(x=60,y=290,height=50,width=380)

lab_up=Label(root,text="00",font=("Bahnschrift Condensed",30,"bold"),bg="blue",fg="white")
lab_up.place(x=60,y=360,height=50,width=380)

button=Button(root,text="Check Speed",font=("Bahnschrift Condensed",30,"bold"),relief=RAISED,bg="green",fg="white",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

root.mainloop()