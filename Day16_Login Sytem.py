from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.geometry("300x200")
root.title("Login System")

def login():
    a=email.get()
    b=password.get()
    if (b=="123"):
        messagebox.showinfo("Success","Login Successfull!")
    else:
        messagebox.showerror("Failed","Login Failed!")


Label(root,text="Email ID").pack()
email=ttk.Entry(root)
email.pack(pady=10)

Label(root,text="Password").pack()
password=ttk.Entry(root,show="*")
password.pack(pady=10)

ttk.Button(root,text="Login!",cursor="hand2",command=login).pack(pady=10)
root.mainloop()
