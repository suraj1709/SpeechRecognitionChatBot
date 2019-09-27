# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:29:44 2019

@author: suraj
"""

import os
#Install Playsound libary for playing an audio in python(pip install playsound)
import playsound
##Install SpeechRecognition libary for translate speach to text in python(pip install SpeechRecognition)
import speech_recognition as sr
##Install gTTS libary for translate text to speach in python(pip install gTTS)
from gtts import gTTS
#Generating random value
import random
#Opening web browser
import webbrowser


# Speak function is used to get the tex from user transalte it to mp3 file using gTTS module and play using soundplay libary 
def speak(text):
        tts=gTTS(text=text,lang="en")
        r1 = random.randint(1,10000000)
        r2 = random.randint(1,10000000)
        filename=str(r1)+"voice"+str(r2)+".mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

#get_audio function get the input from user through microphone translate it into text
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source,phrase_time_limit=10)
        said=""
        try:
            said=r.recognize_google(audio ,language='en-US')
            print(said)
           
        except :
            speak("Could not understand your audio, PLease try again!")
        return said
   
# search_web function help user to search in youtube or google as per user command
def search_web(input):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if 'youtube' in input:
        speak("Opening Youtube")
        indexs=input.lower().split().index('youtube')
        query=input.split()[indexs+1:]
        webbrowser.get(chrome_path).open("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return
    elif 'google' in input:
        speak("Opening Google")
        indexs=input.lower().split().index('google')
        query=input.split()[indexs+1:]
        webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + '+'.join(query))
        return
    elif 'search' in input:
        speak("Opening Google")
        indexs=input.lower().split().index('search')
        query=input.split()[indexs+1:]
        webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + '+'.join(query))
        return
    
    
#open_application function help user to open an application as per user command  
def open_application(input):
    if "chrome" in input:
        speak("Opening Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    else:
        speak("Application not available")
        return
    
#process_input function help some of query asked by the user to help 
def process_input(input):
    try:
        if 'who are you' in input or 'name' in input:
            speak_input='My name is Pixie I am here to help you'
            speak(speak_input)
            return
        elif 'about yourself' in input or 'tell me something' in input:
            speak_input='My name is Pixie I am a robot here to help you make your life easy '
            
        elif 'open' in input or 'file' in input:
            open_application(input)
            return
        elif 'search' in input or 'play' in input:
            search_web(input)
            return
        else:
            speak("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except :
      speak("I don't understand, I can search the web for you, Do you want to continue?")
      ans = get_audio()
      if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
#Main Function 
if __name__=="__main__":
    speak("Hello Human")
    while(1):
        speak('what can i do for you ?')
        text=get_audio()
        if text==0:
            continue
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
                speak("Ok bye, Human")
                break
        process_input(text)
        
    
            
        
            
        
            
            
            
    
    
        
        

