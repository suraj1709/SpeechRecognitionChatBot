# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:49:19 2019

@author: suraj
"""

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random


def speak(text):
    tts=gTTS(text=text,lang="en")
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    filename=str(r1)+"voice"+str(r2)+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
   

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except:
            speak("Could not understand your audio, PLease try again!")
    return said
def bot():
    text=get_audio() 
    if "hello" in text or "hii" in text :
        speak("Hello Human, How may i help you")
    elif "weather" in text:
        speak("Today Weather is pleasant!!")
    elif "name" in text or "about" in text:
        speak("My name is Pixie !!I am your personal assistant")
    elif "bye" in text or "go" in text or "sleep" in text:
        speak("Bye Human,have a good day !! ")
        
if __name__=="__main__":
    bot()
             

          
    