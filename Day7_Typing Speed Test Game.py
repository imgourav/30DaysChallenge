from tkinter import *
from tkinter import ttk
import random
from timeit import default_timer 
from PIL import Image,ImageTk
import difflib

root=Tk()                                         # Creating Our Main Window
root.geometry("750x500")
root.resizable(0,0)
root.title("Coder.Buzz- Typing Speed Test")

a=ImageTk.PhotoImage(file="background.jpg")
img=Label(root,image=a,bd=0)
img.place(x=0,y=0)

def show():
	global start
	global sentence
	entry.focus_set()					                      # To Focus the Cursor on the Entry Box
	start= default_timer()				                  # To Start the Timer
	f = open('sentences.txt').read()	              # To Fetch Sentences from the .txt file
	sentences = f.split('\n')
	sentence = random.choice(sentences)
	Label(root,text=sentence,font=("Arial",15),bg="#0D1114",fg="white").pack(expand=True)

def check():
	string=f"{entry.get()}"
	end=  default_timer()
	time= round(end-start,2)
	speed=round(len(sentence.split())*60/time,2)

	if string==sentence:
		Msg1= "Time= "+str(time)+" seconds"
		Msg2= "Accuracy= 100%"
		Msg3= "Speed= "+str(speed)+" wpm" 

	else:
		accuracy=difflib.SequenceMatcher(None,sentence,string).ratio()
		accuracy=str(round(accuracy*100,2))
		Msg1= "Time= "+str(time)+ " seconds"
		Msg2= "Accuracy= "+accuracy+"%"
		Msg3= "Speed= " + str(speed) + " wpm" 

	Label(root,font=('Arial',15,'bold'),text = Msg1,bg="#0D1114",fg="white").place(x=500,y=50)
	Label(root,font=('Arial',15,'bold'),text = Msg2,bg="#0D1114",fg="white").place(x=500,y=100)
	Label(root,font=('Arial',15,'bold'),text = Msg3,bg="#0D1114",fg="white").place(x=500,y=150)
	Label(root,font=('Arial',15,'bold'),text="Your Results ---->",bg="#0D1114",fg="white").place(x=200,y=100)

entry=ttk.Entry(root,width=70,font=10)
entry.place(x=60,y=280)
entry.bind("<Return>",lambda e:check())

ttk.Button(root,text="Show Sentence! ",cursor="hand2",command=show).place(x=250,y=350)
ttk.Button(root,text="Done!",cursor="hand2",command=check).place(x=400,y=350)

root.mainloop()
