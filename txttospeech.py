
import os
import boto3
from tkinter import *
from pygame import mixer


root =Tk()
root.title('Speech')


def quit():
    exit()


def insert_command():
    polly_clint=boto3.Session(
    aws_access_key_id='######################',
        aws_secret_access_key='###################################',
        region_name='ap-south-1').client('polly')
    spoken_text=polly_clint.synthesize_speech(Text=txt.get(),OutputFormat='mp3',VoiceId='Aditi')
    with open('music.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()

def play():
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()

def remove_audio():
    while mixer.music.get_busy() == True:
        pass
    mixer.quit()
    os.remove('music.mp3')




data=StringVar()
txt=Entry(root,width='60')
txt.grid(row=0,column=0)
b1=Button(root,text='Run',command=insert_command,width='15')
b1.grid(row=1,column=1)
b2=Button(root,text='play',command=play,width='15')
b2.grid(row=2,column=1)
b3=Button(root ,text='Exit' , command=quit,width='15')
b3.grid(row=3,column=1)
b4=Button(root ,text='Delete' , command=remove_audio,width='15')
b4.grid(row=4,column=1)

options=[
    'Aditi','Emma','Naja','Lotte','Nicole','Amy','Ivy'
]
voice = StringVar(root)
voice.set(options[0])# default value
opt = OptionMenu(root, voice, *options)
opt.grid(row=5,column=1)
mainloop()


mainloop()
