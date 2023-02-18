# DATA STRUCTURE AND ALGORITHMS - FINAL PROJECT
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = tkinter.Tk()

answers=["python","len","fifo",'array','list','data','binary','queues','heap','push','structure','algorithmr']
words=['tohynp','nel','iffo','rraya','ilst','tada','ryanib','ueueqs','peah','upsh','sttrucer','gorialthmr']

num=random.randrange(0,len(words),1)
c=0
d=0
s = ""
l = Label(root)

def reset():
    global words, answers, num
    num=random.randrange(0,len(words),1)
    label.config(text = words[num])
    e1.delete(0, END)

def default():
    global words,answers,num
    label.config(text = words[num])

def checkans():
    global words, answers, num, c, d, s, l
    d=int(d)+1
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("RIGHT","It's the correct answer!!")
        c = int(c)+1
    else:
        messagebox.showerror("WRONG", "It's not the correct answer.")
    s = 'Score :' + str(c) + '/' + str(d)
    l.forget()
    l = Label(root, font=("Agency FB", 30), text=s, bg="#8B0000", fg="#fff", )
    l.pack(side=LEFT)
    reset()


root.geometry("500x500+500+150")
root.title("\nJumbled word game")
root.configure(background="#8B0000")

Label(root,text="JUMBLED WORD GAME",font = ("Agency FB",75),bg = "#8B0000", fg = "#fff").pack(pady = 5)
label = Label(root,font = ("Arial",50),bg = "#FFFFFF", fg = "#8B0000")
label.pack(pady = 30,ipady=10,ipadx=40)

ans = StringVar()
e1 = Entry(root,font = ("Agency FB",20),textvariable = ans,)
e1.pack(ipady=5,ipadx=5)
Button(root,text = "Check",font = ("Agency FB",20),width = 10,bg="#8B0000",fg="#FFFFFF",relief = GROOVE,command = checkans,).pack(pady = 40) #created a submit button
Button(root,text = "Reset",font = ("Agency FB",20),width = 10,bg="#8B0000",fg="#FFFFFF",relief = GROOVE,command = reset).pack() #created a reset button

default()

root.mainloop()