from  tkinter import * 
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("To Do List - @Coder.Buzz")
root.config(bg="cyan")

#............................All Functions.......................
def Add_Task():
    input_text=task.get()
    if input_text=="":
        messagebox.showwarning("Warning!","Please Enter Task!")
    else:
        listbox.insert(END,input_text)

def Delete_Task():
    selected=listbox.curselection()
    listbox.delete(selected[0])

def Marked_Task():
    marked=listbox.curselection()
    temp=marked[0]
    temp_marked=listbox.get(marked)
    temp_marked=temp_marked + " ✔"
    listbox.delete(temp)
    listbox.insert(temp,temp_marked)

#.......................Frame 1 [ListBox + ScrollBar]............
frame1=Frame(root,bg="cyan")
frame1.pack()

listbox=Listbox(frame1,height=15,font="Helvetica",width=40,bg="yellow")  
listbox.pack(side=LEFT,fill=X,padx=10,pady=10)

scrollbar=ttk.Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#.......................Frame 2 [Entry Box + Labels].............
frame2=Frame(root,bg="cyan")
frame2.pack()

task=StringVar()
entry=ttk.Entry(frame2,textvariable=task,width=30)
entry.grid(row=1,column=0)
entry.focus()

# Buttons
ttk.Button(frame2,text="Add task",cursor="hand2",command=Add_Task).grid(row=1,column=1,padx=10)
ttk.Button(frame2,text="Delete Task",cursor="hand2",command=Delete_Task).grid(row=2,column=1,pady=5)
ttk.Button(frame2,text="Mark as Completed! ",cursor="hand2",command=Marked_Task).grid(row=2,column=0,pady=5)

root.mainloop()
