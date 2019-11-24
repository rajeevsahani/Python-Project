#Infinite loop
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    while(1):
        print ('Say Something!')
        audio = r.listen(source)
        print ('Listening completed! Please Wait')
        text = r.recognize_google(audio)
        #text = r.recognize_google(audio,language='hi-IN')
        print("you said: " +text)

