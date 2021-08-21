from time import strftime 
from tkinter import * 
from tkinter import ttk
import time
import datetime
from pygame import mixer
 
root = Tk() 
root.geometry("400x300")
root.config(bg="orange")
root.title('Alarm Clock- @coder.buzz') 

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            mixer.init()
            mixer.music.load(r'C:\Users\vj004\Desktop\sound.mp3')     # Get This Sound Track from our Telgram Channel.
            mixer.music.play()                                        # t.me/coderbuzz or Type coderbuzz on Telegram
            break

Label(root,font=('arial',20,'bold'),text="Set your Alarm!",bg="orange").place(x=100,y=30)
#............................Frame [Labels + Entry Boxes + Button]...............................................
frame=Frame(root,bg="orange")
frame.place(x=50,y=100)

hrs=StringVar()
mins=StringVar()
secs=StringVar()

Label(frame,text="Enter Time in 24 Hours Format..",bg="orange",font=5).grid(row=0,columnspan=3)
ttk.Entry(frame,textvariable=hrs,width=5,font =('arial', 20, 'bold')).grid(row=1,column=0,padx=10)
ttk.Entry(frame,textvariable=mins,width=5,font =('arial', 20, 'bold')).grid(row=1,column=1)
ttk.Entry(frame,textvariable=secs,width=5,font =('arial', 20, 'bold')).grid(row=1,column=2,padx=10)
Button(frame,text="Set Alarm!",cursor="hand2",command=setalarm,height=2,width=10,font=5).grid(row=2,column=1,pady=15)

mainloop() 
