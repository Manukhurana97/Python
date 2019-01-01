# Amazon polly (text to speech)
#package - boto3

import boto3
import os
from pygame import mixer

AB = input("Enter something : ")
polly_clint = boto3.Session( aws_access_key_id='create your key on aws',
    aws_secret_access_key='create your key on aws',
    region_name='ap-south-1').client('polly') # polly instance
spoken_text = polly_clint.synthesize_speech(Text=AB, OutputFormat='mp3', VoiceId='Emma')

# print(spoken_text)

with open('music.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()

while mixer.music.get_busy()==True:
    pass
mixer.quit()
os.remove('music.mp3')
