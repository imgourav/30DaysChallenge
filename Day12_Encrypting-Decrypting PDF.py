from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader

root = Tk()
root.title("PDF Locker")
root.geometry("1000x662")
root.resizable(0,0)

a=ImageTk.PhotoImage(file="image.jpg")                  # Image File is available on Telegram channel
img=Label(root,image=a,bd=0)                            # t.me/coderbuzz or Type coderbuzz on Telegram
img.place(x=0,y=0)

def open_file():
    def encrypt():
        FileName=pdf_file.split(".")[0]
        if pdf_file is not None:
            out = PdfFileWriter()
            file = PdfFileReader(pdf_file)
            num = file.numPages
            for i in range(num):
                page = file.getPage(i)
                out.addPage(page)
            out.encrypt(password.get())
            with open(FileName+"_Encrypted.pdf", "wb") as f:
                out.write(f)
            messagebox.showinfo("Success","File encrypted successfully!")
        else:
            messagebox.showerror("Failed","Unable to encrypt file")

    def decrypt():
        FileName=pdf_file.split("_")[0]
        out = PdfFileWriter()
        file = PdfFileReader(pdf_file)                   
        if file.isEncrypted:
            if (password.get()==""):
                messagebox.showerror("Failed","Please Enter Password to Decrypt!")
            else:
                try:
                    file.decrypt(password.get())
                    for i in range(file.numPages):
                        page = file.getPage(i)
                        out.addPage(page)
                    with open(FileName+"_Decrypted.pdf", "wb") as f:
                        out.write(f)
                    messagebox.showinfo("Success","File Decrypted successfully!")
                except:
                    messagebox.showerror("Failed","Entered Wrong Password!")
        else:
            messagebox.showerror("Failed","File already Decrypted!")

    pdf_file=filedialog.askopenfilename(title="Select a File",filetype=(("pdf files", "*.pdf"),("all files", "*.*")))
    Label(root,text="Selected File:- "+pdf_file,font=5,bg="#002629",fg="white").place(x=250,y=370)
    Button(root,text="Encrypt",command=encrypt,width="15",font=10,cursor="hand2").place(x=300,y=400)
    Button(root,text="Decrypt",command=decrypt,width="15",font=10,cursor="hand2").place(x=600,y=400)

Label(root,text="Select a pdf to Encrypt or Decrypt\n",font=10,bg="#002629",fg="white").place(x=380,y=200)
Button(root,text="Browse file",command=open_file,width="15",height="2",font=10,cursor="hand2").place(x=430,y=230)

Label(root,text="Enter Password to Encrypt or Decrypt\n",font=10,bg="#002629",fg="white").place(x=380,y=300)
password=ttk.Entry(root,show="*",width=20,font=10)
password.place(x=410,y=330)

root.mainloop()
