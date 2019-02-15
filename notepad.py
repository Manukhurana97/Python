import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import pygame


class Notepad:

    #variables
    __root = Tk()


    #default window width and height
    __thisWidth = 650
    __thisHeight = 550
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        # initialization

        # set icon
        try:
        		self.__root.wm_iconbitmap("images.png") #GOT TO FIX THIS ERROR (ICON)3
        except:
        		pass

        # set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # set the window text
        self.__root.title("Untitled - Notepad")

        # center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        # add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New" , command=self._New_File)
        self.__thisFileMenu.add_command(label="Open", command=self._Open_File)
        self.__thisFileMenu.add_command(label="Save" ,command=self._save_file)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self._quit)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad" ,command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        # it is used to print the  text box
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)# scroll bar right
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        # make scrollbar dynamic
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def _New_File(self):
        self.__root.title('Untitled - Notepad')
        self.__file=None
        self.__thisTextArea.delete(1.0,END)

    def _Open_File(self):
        self.__file=askopenfilename(defaultextension="*.*", filetypes=[("All File",'*.*'),("java","*.java"),("Python","*.py"),("javascript","*.js")])
        if self.__file == "":
            # no file is open
            self.file=None
        else:
            self.__root.title(os.path.basename(self.__file)+" Manu")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file)
            self.__thisTextArea.insert(1.0,file.read())
            file.close()

    def _save_file(self):
        if self.__file == None:
             #save file
             self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt" ,  filetypes=[("All File",'*.*')])

             if self.__file =="":
                self.__file=None
             else:
                 file=open(self.__file,'w')
                 file.write(self.__thisTextArea.get(1.0,END))
                 file.close()
                 # change the window title
                 self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
             file = open(self.__file, "w")
             file.write(self.__thisTextArea.get(1.0, END))
             file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def _quit(self):
        exit()

    def __showAbout(self):
        showinfo("Notepad 1,0", "Created by: Manu khurana")

    def run(self):
        self.__root.mainloop()

notepad = Notepad()
notepad.run()
