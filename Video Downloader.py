import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog
import youtube_dl as yd
import sys

# YouTube('https://www.youtube.com/watch?v=jFGKJBPFdUA&list=RDjFGKJBPFdUA&start_radio=1').streams.first().download("/Users/manukhurana/Desktop")


def createwidgets():

    label = Label(root, text="Enter the video link")
    label.grid(row=0, column=0, pady=5, padx=5)

    root.linktext = Entry(root, width=40)
    root.linktext.grid(row=0, column=1, pady=3, padx=3, columnspan = 1)

    destinationLabel = Label(root, text="Save Audio in")
    destinationLabel.grid(row=2, column=0, padx=5, pady=5)

    root.destinationtext=Entry(root,width=40)
    root.destinationtext.grid(row=2, column=1, padx=5, pady=5)

    browserButton = Button(root, text="Browse",command=Browse, width=15)
    browserButton.grid(row=2, column=2, padx=5, pady=5)

    Downloadbutton = Button(root, text="Download Video", command=Downloadvideo, width=30)
    Downloadbutton.grid(row=3, column=0, padx=5)

    Downloadbutton = Button(root, text="Download Audio", command=Downloadaudio, width=30)
    Downloadbutton.grid(row=3, column=1, padx=5)

def Browse():
    # Retrieving the user-input destination directory
    root.destination= filedialog.askdirectory()

    # Displaying the directory in the directory textbox
    root.destinationtext.insert('0', root.destination)

def Downloadvideo():

    YouTube(root.linktext.get()).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(root.destination)
    messagebox.showinfo("Success","Video Downloadad and Saved in "+root.destination)



def Downloadaudio():
    videoLink = root.linktext.get()
    savePath = root.destinationtext.get()

    # Specifying the options for downloading
    audDWLDopt = {

        'format': 'bestaudio/best',
        'outtmpl': savePath + "/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320'
        }],
    }
    # Downloading the audio file
    with yd.YoutubeDL(audDWLDopt) as aud_dwld:
        aud_dwld.download([videoLink])
        messagebox.showinfo("Success", "Audio Downloadad and Saved in " + savePath)
        sys.exit(0)


root = Tk()

root.title("YouTube video Downloader")
root.resizable(FALSE, FALSE)
createwidgets()
root.mainloop()
