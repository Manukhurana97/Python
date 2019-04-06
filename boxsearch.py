import sys
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

root =Tk()
ment=StringVar()

def google():
    mtext = ment.get()  # get the value store in ment
    # search
    driver = webdriver.Chrome("C:\\Users\\Manu khurana\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com")
    elem = driver.find_element_by_name("q")  # name of the search bar
    elem.clear()
    elem.send_keys(mtext)  # this is used to send the data/key
    elem.send_keys(Keys.RETURN)  # this is used to written the data/key
    assert "No result found." not in driver.page_source

    mlabel2 = Label(root, text=mtext).pack()
    return

def youtube():
    mtext = ment.get()  # get the value store in ment
    #search
    driver=webdriver.Chrome("C:\\Users\\Manu khurana\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.youtube.com")
    elem = driver.find_element_by_name("search_query")
    elem.clear()
    elem.send_keys(mtext)
    elem.send_keys(Keys.RETURN)
    assert "NO result found"
    mlabel2 = Label(root, text=mtext).pack()
    return

root.geometry('400x400')
root.title("MY personal search")
mlabel=Label(root,text="my label" ).pack()
mEntry=Entry(root,textvariable=ment).pack()
mbutton=Button(root,text="google search" ,command=google).pack()
mbutton=Button(root,text="youtube search" ,command=youtube).pack()
mainloop()







