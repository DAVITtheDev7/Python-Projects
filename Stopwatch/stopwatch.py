
from tkinter import *
from datetime import datetime

temp = 0
after_id = ''


def tick():

    global temp, after_id

    after_id = window.after(1000, tick)

    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")

    label1.configure(text = str(f_temp))

    temp += 1


def start():

    startButton.grid_forget()
    stopButton.grid(row = 1, columnspan = 2, sticky = "ew")

    tick()


def stop():
    stopButton.grid_forget()
    resumeButton.grid(row = 1, column = 0, sticky = "ew")
    resetButton.grid(row = 1, column = 1, sticky = "ew")

    window.after_cancel(after_id)


def resume():
    resumeButton.grid_forget()
    resetButton.grid_forget()
    stopButton.grid(row = 1, columnspan = 2, sticky = "ew")

    tick()


def reset():
    global temp

    temp = 0

    label1.configure(text = "00:00")

    resumeButton.grid_forget()
    resetButton.grid_forget()
    startButton.grid(row = 1, columnspan = 2, sticky = "ew")



window = Tk()

window.title("Stopwatch")

label1 = Label(window, width = 5, font = ("Verdana", 100), text = "00:00")
label1.grid(row = 0, columnspan = 2)

startButton = Button(window, text = "START", font = ("Verdana", 30), command = start)
stopButton = Button(window, text = "STOP", font = ("Verdana", 30), command = stop)
resumeButton = Button(window, text = "RESUME", font = ("Verdana", 30), command = resume)
resetButton = Button(window, text = "RESET", font = ("Verdana", 30), command = reset)

startButton.grid(row = 1, columnspan = 2, sticky = "ew")

window.mainloop()

