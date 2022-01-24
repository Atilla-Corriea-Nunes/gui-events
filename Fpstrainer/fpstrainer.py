from cgitb import text
from distutils import command
import random
import tkinter
from tkinter.ttk import Label
import os
import sys


timeleft = 20
prompts = ["Press: W", "Press: A", "Press: D", "Press: S", "Press: Space", "Single click", "Double click", "Triple click"]
playerscore = 0
randomchoice = random.choice(prompts)
y = 0


def resetGame():
    global timeleft, prompts, playerscore, randomchoice, y
    timeleft = 20
    prompts = ["Press: W", "Press: A", "Press: D", "Press: S", "Press: Space", "Single click", "Double click", "Triple click"]
    playerscore = 0
    randomchoice = random.choice(prompts)
    y = 0
    

def place_button(event=""):
    global promptbutton, randomchoice, playerscore
    try:
        window.unbind(currentbind)
        promptbutton.unbind(currentbind)
        if "Press" in randomchoice:
            playerscore += 1
        else:
            playerscore += 2
        promptbutton.destroy()
    except:
        pass
    scorecounter.configure(text= str(playerscore) + " Points")
    randomchoice = random.choice(prompts)
    promptbutton = tkinter.Label(text=randomchoice)
    whatToBind()
    randomlocationy = random.randint(0,450)
    randomlocationx = random.randint(0,400)
    promptbutton.place(x=randomlocationx, y=randomlocationy)


def bindVar(var):
    if var == "Press: W":
        return "w"
    elif var == "Press: A":
        return "a"
    elif var == "Press: D":
        return "d"
    elif var == "Press: S":
        return "s"
    elif var == "Press: Space":
        return "<space>"
    elif var == "Single click":
        return "<Button-1>"
    elif var == "Double click":
        return "<Double-Button-1>"
    elif var == "Triple click":
        return "<Triple-Button-1>"

def whatToBind():
    global randomchoice, currentbind
    currentbind = bindVar(randomchoice)
    if "Press" in randomchoice:
        window.bind(currentbind, place_button)
    else:
        promptbutton.bind(currentbind,place_button)


def startTheGame():
    global y, top, firsttime

    try:
        top.destroy()
    except:
        pass
    resetGame()
    startbutton.destroy()
    window.after (1000,subtractTime)
    place_button()


def subtractTime():
    global timeleft, window, y, top
    if timeleft > 0:
        timeleft -= 1
    else:
        
        if y == 0:
            top = tkinter.Toplevel(window)
            top.title("Game over")
            top.geometry("400x100")
            label2 = tkinter.Label(top,text="Game over, you managed to score "+ str(playerscore) +" points! Do you want to restart?")
            label2.pack(pady=10)
            frame = tkinter.Frame(top)
            frame.pack(pady=5)
            yes = tkinter.Button(frame, text="YES", command=lambda: os.execl(sys.executable, os.path.abspath(__file__), *sys.argv))
            yes.pack()
            no = tkinter.Button(frame, text="NO", command=quit)
            no.pack()
            
            y += 1

    l.configure(text="Time remaining: "+ str(timeleft))
    window.after (1000,subtractTime)

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=500,height=500)
canvas.pack(fill="both", expand=True)
startbutton = tkinter.Button(canvas)
startbutton.configure(text="Press to start", command=startTheGame)
startbutton.pack()
startbutton.place(x=210, y=250)


l = tkinter.Label(text="Time remaining: "+ str(timeleft))
l.pack()

scorecounter = tkinter.Label(text= str(playerscore) + " Points")
scorecounter.pack()



window.mainloop()
print(playerscore)