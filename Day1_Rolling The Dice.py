from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry('400x400')
root.config(bg="white")
root.title('Roll The Dice with @Coder.buzz')

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = Label(root, image=image1,bd=0)
label1.image = image1 
label1.pack(expand=True)

def roll_the_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)   
    label1.image = image1


button = Button(root, text='Roll the Dice', command=roll_the_dice)
button.pack(expand=True)

root.mainloop()


# STEP 1: Download the Images from Telegram Channel.
# STEP 2: Images and Python File must be in the same directory/folder.
# STEP 3: Run the Code :)
