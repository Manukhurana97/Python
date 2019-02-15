# Internet Check

from requests import get,exceptions

try:
     get('https://www.google.com/',timeout=2)
     print('connected')
except:
     print('Not connected')



# cpu and memmory

import psutil

#print(psutil.cpu_percent(interval=1,))# cpu usage
#print(psutil.cpu_count()) #cpu count


#print(psutil.virtual_memory())# memory

#print(psutil.disk_partitions()) # show disk partition

#print(psutil.net_connections()) # show connections

battery=psutil.sensors_battery() # battery percentage
print(battery)

plugged=battery.power_plugged
if plugged:
    print('Plugged')
else:
    print('Not Plugged')


#print(psutil.sensors_temperatures()) # computer computer








from tkinter import *

# root=Tk()
# root.geometry('400x400')
#
# def internet():
#     try:
#         get('https://www.google.com/',timeout=2)
#         label=Label(root, text='connected')
#         label.grid()
#     except:
#         label1 = Label(root, text='Not connected')
#         label1.grid()
#
#
#
# b=Button(root, text='Check', command=internet)
# b.grid()
#
# root.mainloop()




