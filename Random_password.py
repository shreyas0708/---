import tkinter as tk
from tkinter import *
import random
import string as str
import pyperclip
import re

FONT1 = ("Montserrat",20)
FONT2 = ("Consolas",14)
FONT3 = ("Panton",10)

BG = "#fe5114"
BG_BUTTON = "white"
FG = "white"

LOWER = str.ascii_lowercase
UPPER = str.ascii_uppercase
DIGITS = str.digits
SPECIAL = str.punctuation

def complexityChecker():
    if (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        complexity_res.config(text = "Password is strong")

    else:
        complexity_res.config(text='Recommended to generate a stronger password')

def passwdGenerator():
    global password
    password = random.choice(UPPER)+random.choice(LOWER)+random.choice(DIGITS)+random.choice(SPECIAL)
    length = int(passwd_len.get())
    for iter in range(length-4):
        password += random.choice(LOWER+UPPER+DIGITS+SPECIAL)

    gen_passwd.config(text=password)
    complexityChecker()


def copyToClipboard():
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")
root.config(background=BG)
root.geometry("600x300+700+250")

lab1 = Label(root, text="RANDOM PASSWORD GENERATOR",font=FONT1,foreground = "White", bg=BG)
lab1.pack(pady=10)

passwd_lab = Label(root, text="Password length =",font=FONT2,foreground=FG,bg= BG)
passwd_lab.place(x=15,y=65)

passwd_len = IntVar()
len = Spinbox(root, from_=8, to_=32, textvariable=passwd_len,width=3,font=FONT3)
len.place(x=180,y=71.5)

generate = Button(root, text="Generate", command=passwdGenerator,font=FONT2,bg=BG_BUTTON,foreground=BG)
generate.place(x=25, y=115)

strength = Label(root, text="Complexity : ", font=FONT2,bg=BG,foreground=FG)
strength.place(x=25,y=165)

copy = Button(root, text="Copy to clipboard",command=copyToClipboard, font=FONT2, bg=BG_BUTTON, foreground=BG)
copy.place(x=25,y=215)

gen_passwd = Label(root,font=FONT2,background=BG,foreground=FG)
gen_passwd.place(x=150, y=115)

complexity_res = Label(root,font=FONT2,background=BG,foreground=FG)
complexity_res.place(x=140, y=165)

root.mainloop()

