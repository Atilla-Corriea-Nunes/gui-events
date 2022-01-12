import tkinter
import random

wonitem = ""
counter = 0

def makeyellow(event):
    window.configure(bg="yellow")

def changeback(event):
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")

def countUp():
    global counter
    counter += 1
    l.configure(text=counter)
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")

def countDown():
    global counter
    counter -= 1
    l.configure(text=counter)
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")


window = tkinter.Tk()
window.configure(bg="grey")

u = tkinter.Button(window)
u.configure(text="Up", command=countUp,padx=140, pady=12)
u.pack(pady=20)

l = tkinter.Label(text=counter, padx=145, pady=12)
l.pack(pady=20)
l.bind("<Enter>", makeyellow)
l.bind("<Leave>", changeback)

d = tkinter.Button(window)
d.configure(text="Down",command=countDown,padx=132, pady=12)
d.pack(pady=20)


window.title("Clicker")

window.mainloop()