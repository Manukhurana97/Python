from requests import  get
from requests import exceptions
from tkinter import *
import time
import pyspeedtest
import sys
import psutil



root=Tk()


def checkinternet():
    print()
    try:
        get('https://google.com',timeout=2)
        global label
        Label(text='Internet Connected',fg='green').grid(row=1,column=1)

        st = pyspeedtest.SpeedTest()
        ds = st.download()
        ds = ds / (1024 * 1024)
        Label(text="Download speed (Mb/S)", fg='green').grid(row=2, column=0)
        Label(text = ds, fg='green').grid(row=2,column=1)

        us = st.upload()
        us = us / (1024 * 1024)
        Label(text="Upload speed (Mb/S)", fg='green').grid(row=3, column=0)
        Label(text=us, fg='green').grid(row=3,column=1)

        zz = psutil.cpu_percent()
        Label(text="Cpu Usage (%)", fg='green').grid(row=4, column=0)
        Label(text=zz, fg='green').grid(row=4, column=1)

        battery=psutil.sensors_battery()
        Label(text="Battery (%)", fg='green').grid(row=9, column=0)
        Label(text=battery, fg='green').grid(row=9, column=1)

        disk=psutil.cpu_count()
        Label(text=" Cpu count", fg='green').grid(row=6, column=0)
        Label(text=disk, fg='RED').grid(row=6, column=1)

        # sensors_temperatures = psutil.sensors_temperatures()
        # Label(text=" sensors_temperatures(Feh)", fg='green').grid(row=11, column=0)
        # Label(text=sensors_temperatures, fg='RED').grid(row=7, column=1)

        cpu_times = psutil.cpu_times()
        Label(text=" cpu_times", fg='green').grid(row=7, column=0)
        Label(text=cpu_times, fg='RED').grid(row=7, column=1)

        virtual_memory = psutil.virtual_memory()
        Label(text=" virtual_memory", fg='green').grid(row=9, column=0)
        Label(text=virtual_memory, fg='RED').grid(row=9, column=1)

        # sensors_fans = psutil.sensors_fans()
        # Label(text=" sensors_fans", fg='green').grid(row=10, column=0)
        # Label(text=sensors_fans, fg='RED').grid(row=11, column=1)

        disk_partitions = psutil.disk_usage('/')
        Label(text=" Total size", fg='green').grid(row=10, column=0)
        Label(text=" Used Memmory (GB)", fg='green').grid(row=11, column=0)
        Label(text=" Free Mennory (GB)", fg='green').grid(row=12, column=0)
        Label(text=(disk_partitions.total/(1024.0 ** 3)), fg='RED').grid(row=10, column=1)
        Label(text=(disk_partitions.used/(1024.0 ** 3)), fg='RED').grid(row=11, column=1)
        Label(text=(disk_partitions.free/(1024.0 ** 3)), fg='RED').grid(row=12, column=1)




    except exceptions.ConnectionError:
        Label(root,text='Internet Not connected',fg='red').grid()

def quit():
    root.destroy()
    sys.exit()




b = Button(root, text='Check', command=checkinternet, fg='blue',padx=5,pady=5).grid(row=0,column=0)
b1 = Button(root,text='Exit',command=quit, fg='blue',padx=5,pady=5).grid(row=0, column=1)
root.mainloop()

