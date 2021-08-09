from tkinter import *
import datetime
from PIL import Image,ImageTk
from tkinter import ttk

#Creating Main window
root = Tk()
root.geometry('1019x500')
root.resizable(0,0)
root.title('Age Calculator')

a=ImageTk.PhotoImage(file="image.png")          # Download Image File from Telegram Channel
img=Label(root,image=a,bd=0)                    # t.me/coderbuzz
img.place(x=0,y=0)

def calculate():
    birth_year=int(yearEntry.get())
    name=nameEntry.get()
    birth_month=int(monthEntry.get())
    birth_day=int(dayEntry.get())

    today = datetime.date.today()
    year=today.year
    month=today.month
    day=today.day

    month_values =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    if (birth_day > day): 
        month = month - 1
        day = day + month_values[birth_month-1] 

    if (birth_month > month): 
        year = year - 1
        month = month + 12

    cal_day = day - birth_day; 
    cal_month = month - birth_month; 
    cal_year = year - birth_year; 

    result="Hey "+name+"! You are " + str(cal_year)+ " Years " +str(cal_month)+" Months " +str(cal_day)+ " Days old!!!"
    text=Text(root,width=60,height=1,font=10)
    text.insert(END,result)
    text.config(state='disabled')
    text.place(x=400,y=150)

Label(root,text="** Age Calculator **",font=("Helvetica",20),bg="white").place(x=400,y=30)
frame=Frame(root,bg="white")
frame.place(x=150,y=100)

Label(frame,text = "Name",bg="white",font=10).grid(column=0,row=1)
Label(frame,text = "Year",bg="white",font=10).grid(column=0,row=2)
Label(frame,text = "Month",bg="white",font=10).grid(column=0,row=3)
Label(frame,text = "Day",bg="white",font=10).grid(column=0,row=4)

nameEntry = ttk.Entry(frame)
nameEntry.grid(column=1,row=1,padx=10)
yearEntry = ttk.Entry(frame)
yearEntry.grid(column=1,row=2,pady=10)
monthEntry = ttk.Entry(frame)
monthEntry.grid(column=1,row=3,padx=10)
dayEntry = ttk.Entry(frame)
dayEntry.grid(column=1,row=4,pady=10)

ttk.Button(root,text="Calculate!",cursor="hand2",command=calculate).place(x=250,y=230)
root.mainloop()
