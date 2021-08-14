from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import base64

root = Tk()
root.geometry('750x422')
root.resizable(0,0)

z=ImageTk.PhotoImage(file="image.jpg")				# Get the Image File from the Telegram Channel
img=Label(root,image=z,bd=0)					# t.me/coderbuzz or type coderbuzz on Telegram
img.place(x=0,y=0)

#title of the window
root.title("CoderBuzz- Encode and Decode")
Label(root, text ='ENCODE    \nDECODE!', font = 'arial 20 bold',bg="#FFDB45").place(x=40,y=150)

result_encode=StringVar()
result_decode=StringVar()
encode_text=StringVar()
decode_text=StringVar()

def reset():
	result_encode.set("")
	result_decode.set("")
	encode_text.set("")
	decode_text.set("")

def ENCODE():
	b=encode.get()
	c=base64.b64encode(b.encode("utf-8"))
	result_encode.set(c)

def DECODE():
	e=decode.get()
	f=base64.b64decode(e)
	result_decode.set(f)

Label(root,text="Enter your Secret Msg here!",bg="#F6E7C0").place(x=380,y=130)
encode=ttk.Entry(root,textvariable =encode_text,width=25,font=10)
encode.place(x=380,y=150)
ttk.Button(root,text="Encode",cursor="hand2",command=ENCODE).place(x=620,y=150)

Label(root,text="Enter your ENCODED Msg here!",bg="#F6E7C0").place(x=380,y=230)
decode=ttk.Entry(root,textvariable =decode_text,width=25,font=10)
decode.place(x=380,y=250)
ttk.Button(root,text="Decode",cursor="hand2",command=DECODE).place(x=620,y=250)

ttk.Entry(root,textvariable=result_encode,width=35,font=10).place(x=380,y=200)
ttk.Entry(root,textvariable=result_decode,width=35,font=10).place(x=380,y=300)
ttk.Button(root,text="Reset",cursor="hand2",command=reset).place(x=450,y=350)

root.mainloop()
