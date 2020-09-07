from tkinter import *
from pytube import YouTube
from pytube import Playlist
from tkinter import messagebox
import os
import pafy


def create_widgets():

    label = Label(root, text="Url")
    label.grid(row=0, column=0, pady=0, padx=0)

    root.link_text = Entry(root, width=50)
    root.link_text.grid(row=0, column=1, pady=5, padx=15, columnspan=1)

    download_video = Button(root, text="Download Video", command=Download_video, width=25, fg='white')
    download_video.grid(row=2, column=0, padx=5)

    download_audio = Button(root, text="Download Audio", command=Download_audio, width=25, fg='white')
    download_audio.grid(row=2, column=1, padx=5)

    download_playlist = Button(root, text="Download Playlist", command=Download_playlist, width=25,  bg='black')
    download_playlist.grid(row=2, column=2, padx=5)


def Download_video():
    loc = os.getcwd()
    YouTube(root.link_text.get()).streams.filter(adaptive=True).filter(subtype='mp4').order_by(
        'resolution').desc().first().download(loc)
    messagebox.showinfo("Success", "Video Downloadad and Saved in " + loc)


def Download_playlist():
    loc = os.getcwd()
    Playlist(root.link_text.get()).download_all(loc)
    messagebox.showinfo("Success", "Entire Playlist download at " + loc)


def Download_audio():
    loc = os.getcwd()
    audio_Link = root.link_text.get()
    audio = pafy.new(audio_Link)
    best_audio = audio.getbestaudio()
    best_audio.download()
    messagebox.showinfo("Success", "Audio Saved at " + loc)


root = Tk()


root.title("YouTube video Downloader")
root.resizable(FALSE, FALSE)
create_widgets()
root.mainloop()
