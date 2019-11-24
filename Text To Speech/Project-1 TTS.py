from gtts import gTTS
from os import system
text=input("Enter your text to convert into MP3:")
obj=gTTS(text,lang='en')
obj.save('deeksha.mp3') # save as mp3
#pip install playsound
from playsound import playsound
playsound('deeksha.mp3')
