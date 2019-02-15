import pyautogui
from tkinter import *

root=Tk()
running=True
def mouse():
    for i in range(5):
        # pyautogui.moveTo(100, 200, duration=.5)
        # pyautogui.moveTo(1000, 800, duration=.5)
        pyautogui.typewrite('hello to all')
        global running
        running=True

def stop():
    global running
    running=False

b1=Button(root, text='Mouse', width=15, command=mouse)
b1.grid(row=0,column=0)
b2=Button(root, text='Stop', width=15, command=stop)
b2.grid(row=0, column=1)
mainloop()