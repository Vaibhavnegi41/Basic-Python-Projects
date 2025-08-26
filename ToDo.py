import customtkinter as ctk

def add_task():
    data=entry.get()
    lab=ctk.CTkLabel(sf,text=data)
    lab.pack()
    entry.delete(0,ctk.END)

root=ctk.CTk()
root.geometry("750x500")
root.title("ToDo App")

lab=ctk.CTkLabel(root,text="Daily task schedule",font=ctk.CTkFont(size=30,weight="bold"))
lab.pack(padx=10,pady=(40,20))

sf=ctk.CTkScrollableFrame(root,width=500,height=270)
sf.pack()

entry=ctk.CTkEntry(sf,placeholder_text="Add Tasks")
entry.pack(fill='x')

btn=ctk.CTkButton(root,text="Add Task",width=500,command=add_task)
btn.pack(pady=20)
root.mainloop()
