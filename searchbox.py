#selenium

import sys
from tkinter import *
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


root =Tk()
ment=StringVar()
pswd=StringVar()


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
#database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="python"
    )
    mycursor = mydb.cursor()
    sql = "insert into search(google,youtube,name) values(%s,%s,%s)"
    val = (mtext , "" , "google")
    mycursor.execute(sql, val)
    mydb.commit()  # its used to make update in mysql
    mydb.close()
    mlabel2 = Label(root, text=mtext).pack()
    return

    #youtube search
def youtube():
    mtext = ment.get()  # get the value store in ment
    #search
    driver=webdriver.Chrome("C:\\Users\\Manu khurana\\Downloads\\chromedriver_win32\\chromedriver.exe" )
    driver.get("https://www.youtube.com")
    elem = driver.find_element_by_name("search_query")
    elem.clear()
    elem.send_keys(mtext)
    elem.send_keys(Keys.RETURN)
    assert "NO result found"
#database
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='python'
    )
    mycursor = mydb.cursor()
    sql = "insert into search(google,youtube,name) values(%s,%s,%s)"
    val = (" ",mtext,"youtube")
    mycursor.execute(sql, val)
    mydb.commit()  # its used to make update in mysql
    mydb.close()
    mlabel2 = Label(root , text=mtext).pack()
    return



def history(event = None):
    root1 = Tk()
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= 'root',
        database='python'
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from search ")
    for x in mycursor:
        mlabel3 = Label(root1, text=x ,padx=30).pack()
       # root1.geometry('400x400')
        root1.title("MY personal search")
    mydb.close()
    mainloop()


root.geometry('400x300')
root.title("MY personal search")
mlabel=Label(root,text="Enter search" ).pack()
mEntry=Entry(root,textvariable=ment , width='35').pack()
mbutton=Button(root,text="google search" ,command=google , padx=5 , pady=5).pack()
mbutton=Button(root,text="youtube search" ,command=youtube , padx='').pack()
mbutton=Button(text="history" , command=history).pack()

mainloop()







