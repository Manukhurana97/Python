from backend import database
import tkinter
from tkinter import *

datas=database()

def get_selected_row(event):
    global selected_tuple
    index = textarea.curselection()[0]
    print(index)
    selected_tuple = textarea.get(index)
    print(selected_tuple[4])
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])



def view_command():
    textarea.delete(0,END)
    for r in datas.search_all():
        textarea.insert(END, r)

def insert_command():
    datas.insert(name.get(), title.get(), edition.get(), isbn.get())
    textarea.delete(0, END)
    textarea.insert(END, (('book'), name.get(), ('successfully inserted into record')))

def delete_command():
    datas.delete(selected_tuple[4])
    textarea.delete(0, END)
    textarea.insert(END, (selected_tuple[1],'sucessfully deleted from record'))

def update_command():
      datas.update(selected_tuple[4],name.get(),title.get(),edition.get(),isbn.get())
      textarea.delete(0, END)
      textarea.insert(END, ('Record sucessfully updated'))


def close_app():
    exit()





root=Tk()
root.title('Book record')
root.geometry('450x300')
name=StringVar()
title=StringVar()
edition=StringVar()
isbn=StringVar()


title1=Label(root, text='Name')
title1.grid(row=0, column=0)
entry1=Entry(root, width='25',textvariable=name)
entry1.grid(row=0, column='1')

title2=Label(root, text='Title')
title2.grid(row=0, column=2)
entry2=Entry(root, width='25',textvariable=title)
entry2.grid(row=0, column='3')

title3=Label(root,text='Edition')
title3.grid(row=1, column=0)
entry3=Entry(root, width='25',textvariable=edition)
entry3.grid(row=1,column='1')

title4=Label(root, text='ISBN')
title4.grid(row=1, column=2)
entry4=Entry(root, width='25',textvariable=isbn)
entry4.grid(row=1, column='3')


textarea=Listbox(root,width=37,height=15)
textarea.grid(row=4,column=0 ,rowspan=50,columnspan=2)

slider=Scrollbar(root)
slider.grid(row=5, column=2)

textarea.configure(yscrollcommand=slider.set)
slider.configure(command=textarea.yview)

textarea.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(root,text='search all' , command=view_command,width=12)
b1.grid(row=4, column='3')
b1=Button(root, text='Update entry',width=12,command=update_command)
b1.grid(row=5, column='3')
b1=Button(root, text='Insert entry',command=insert_command,width=12)
b1.grid(row=6, column='3')
b1=Button(root, text='delete entry', command=delete_command,width=12)
b1.grid(row=7, column='3')
b1=Button(root, text='Close' ,command=close_app,width=12)
b1.grid(row=8, column='3')



mainloop()