#libraries
import pyttsx3

#functions
def speak(text):
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()





#main program

Speak("Hello, I am Jarvis")