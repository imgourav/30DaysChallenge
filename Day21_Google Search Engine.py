# GET ALL THE IMAGE FILES FROM THE TELEGRAM CHANNEL 
# t.me/coderbuzz or type coderbuzz on Telegram.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date               # To Show Date-Time
import webbrowser                       # To open Browser               pip install pycopy-webbrowser
import googlesearch                     # To Run search Commands        pip install google
import urllib.request                   # To Check Internet 


window=Tk()
window.geometry("900x600")
window.resizable(False,False)
window.title("Google Search Engine")                                    # Title
background_image=ImageTk.PhotoImage(file="background.jpg")              #importing Background Image
Label(window,image=background_image,borderwidth=0).place(x=0,y=0)

#################################################### ** Defining Functions ** ######################################################
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def openbrowser(url):                   # To open Browser
    webbrowser.open(url)

def search():
    query = search_box.get("1.0","end-1c")
    s = googlesearch.search(query, tld="co.in", num=10, stop=1, pause=2)
    for j in s: 
        webbrowser.open(j)

#####################################################################################################################################
today=date.today()
Label(window,text=today.strftime("%B %d, %Y"),bg="#E8E9E4",font=("Aerial",10)).place(x=40,y=255)

################################################## ** Google Search Engine ** #######################################################
google_logo=ImageTk.PhotoImage(Image.open("google logo.png"))
Label(window,image=google_logo,borderwidth=0,bg="#E8E9E4").place(x=190,y=160)

search_box=Text(window,width=70,height=1,font=("Aerial",11))
search_box.place(x=40,y=280)
search_box.focus_set()
search_box.bind("<Return>",lambda e:search())

ttk.Button(text="Google Search",width=20,command=search,cursor="hand2").place(x=120,y=320)
ttk.Button(text="I'm Feeling Lucky",width=20,cursor="hand2",command=lambda: openbrowser("https://www.google.com/doodles")).place(x=410,y=320)

Label(text="Google offered in: ",bg="#E8E9E4").place(x=90,y=370)
Label(text="हिन्दी বাংলা తెలుగు मराठी தமிழ் ગુજરાતી ಕನ್ನಡ മലയാളം ਪੰਜਾਬੀ",fg="blue",bg="#E8E9E4").place(x=195,y=370)
#####################################################################################################################################

###################################################### ** Taskbar ** ################################################################
Taskbar=Frame(window,bg="#E9EAE5")
Taskbar.place(x=0,y=0)

google_b=Button(Taskbar,text="Google",bd=0,cursor="hand2",bg="#E9EAE5",font=("Aerial",10),command=lambda: openbrowser("https://www.google.com/"))
google_b.grid(row=0,column=1)

youtube_b=Button(Taskbar,text="Youtube",bd=0,cursor="hand2",bg="#E9EAE5",font=("Aerial",10),command=lambda: openbrowser("https://www.youtube.com/"))
youtube_b.grid(row=0,column=3)

gmail_b=Button(Taskbar,text="Gmail",bd=0,cursor="hand2",bg="#E9EAE5",font=("Aerial",10),command=lambda: openbrowser("https://www.gmail.com"))
gmail_b.grid(row=0,column=5)

drive_b=Button(Taskbar,text="G-Drive",bd=0,cursor="hand2",bg="#E9EAE5",font=("Aerial",10),command=lambda: openbrowser("https://www.drive.google.com"))
drive_b.grid(row=0,column=7)

outlook_b=Button(Taskbar,text="Outlook",bd=0,cursor="hand2",bg="#E9EAE5",font=("Aerial",10),command=lambda: openbrowser("https://outlook.live.com/owa/"))
outlook_b.grid(row=0,column=9)

images_b=Button(Taskbar,text="Images",bd=0,cursor="hand2",bg="#E8E9E4",font=("Aerial",10),command=lambda: openbrowser("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))
images_b.grid(row=0,column=11)

#......................................................** Logo's of Apps **..........................................................
google_logo1=ImageTk.PhotoImage(Image.open("google_logo.png"))
Label(Taskbar,image=google_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=0,padx=5,pady=5)

youtube_logo1=ImageTk.PhotoImage(Image.open("youtube_logo.png"))
Label(Taskbar,image=youtube_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=2)

gmail_logo1=ImageTk.PhotoImage(Image.open("gmail_logo.png"))
Label(Taskbar,image=gmail_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=4)

google_drive_logo1=ImageTk.PhotoImage(Image.open("google_drive_logo.png"))
Label(Taskbar,image=google_drive_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=6,padx=10)

outlook_logo1=ImageTk.PhotoImage(Image.open("outlook_logo.png"))
Label(Taskbar,image=outlook_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=8,padx=10)

google_images_logo1=ImageTk.PhotoImage(Image.open("images_logo.png"))
Label(Taskbar,image=google_images_logo1,borderwidth=0,bg="#E9EAE5").grid(row=0,column=10,padx=10)
#####################################################################################################################################

#################################################### ** Game Button ** ##############################################################
game=ttk.Button(window,text="Play a Game!...",cursor="hand2",command=lambda: openbrowser("https://slither.io"))
game.place(x=290,y=320)
#####################################################################################################################################

#####################################################################################################################################
if connect()==False:
    messagebox.showerror("Warning","Check Your Internet Connection")
    window.destroy()

window.mainloop()
