
from tkinter import *
from tkinter import ttk
import webbrowser

root = Tk()
root.title('Universal Search Bar')
# root.iconbitmap(' ')

style = ttk.Style()
style.theme_use('winnative')

label1 = ttk.Label(root, text='Query')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=50)
entry1.grid(row=0, column=1)

btn2 = StringVar()


def callback():
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q=' + entry1.get())
    elif btn2.get() == 'youtube':
        webbrowser.open('http://duckduckgo.com/?q=' + entry1.get())


def get(event):
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q=' + entry1.get())
    elif btn2.get() == 'youtube':
        webbrowser.open('http://duckduckgo.com/?q=' + entry1.get())




MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=2)

entry1.bind('<Return>', get)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Youtube', value='youtube', variable=btn2)
MyButton3.grid(row=1, column=1, sticky=E)

entry1.focus()
root.mainloop()