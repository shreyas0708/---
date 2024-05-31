import pyttsx3 as pyt 
import speech_recognition as sr 
import os, sys
import datetime
import wikipedia
import webbrowser


WEBSITES = ['youtube','google','wikipedia','instagram','gmail','linkedin','github','google classroom']

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice',voices[0].id) 

def speak(audioMessage):
    engine.say(audioMessage)
    engine.runAndWait()

def greetingsOfTheDay():
    speak("I am TED, your virtual assistant!")
    currentHour = int(datetime.datetime.now().hour)
    if (currentHour >= 0 and currentHour<12):
        speak("TED wishes you a Good Morning!")
    elif (currentHour>=12 and currentHour<18):
        speak("TED wishes you a Good Afternoon!")
    else:
        speak("TED wishes you a Good Evening!")

def userNameInput():
    speak("What is your name?")
    global uName
    uName = takeCommand()
    speak("TED welcomes")
    speak(uName)
    question = f"How can TED help you today, {uName}?"
    speak(question)

def takeCommand():
    rec = sr.Recognizer()
    with  sr.Microphone() as source:
        print("TED is listening...")
        #The pause_threshold parameter is used to determine the minimum length of silence (in seconds) that will be considered a pause in speech. If a pause longer than this threshold is detected, the speech recognition engine will stop listening for further speech.
        rec.pause_threshold = 3 #sec
        audio = rec.listen(source)

    try:
        print("TED is recognizing...")
        query = rec.recognize_google(audio,language='en-in')
        print(f"User said : {query}")

    except:
        print("Unable to Recognise User's voice")
        return "Guest"

    return query

print("Launching TED...")
greetingsOfTheDay()
userNameInput()

while True:
    queryGiven = takeCommand().lower()

    if 'wikipedia' in queryGiven:
        queryGiven = queryGiven.replace("wikipedia",'')
        speak(f"TED is searching Wikipedia for {queryGiven}...")
        res = wikipedia.summary(queryGiven, sentences=1)
        print(res)
        speak(f"According to Wikipedia  , {res}")
    
    elif 'play music' in queryGiven:
        # Add code to play music from a local directory or a streaming service (e.g., Spotify)
        webbrowser.open("spotify.com")

    elif 'website' in queryGiven:
        speak(f"Which website do you want TED to open?")
        queryGiven = takeCommand().lower()

        if queryGiven in WEBSITES:
            speak(f"TED is opening {queryGiven} for you...")
            webbrowser.open(f"{queryGiven}.com")

        else:
            speak("Sorry, TED doesn't have such websites in its database")

    elif 'the time' in queryGiven:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif 'search' in queryGiven:
        queryGiven = queryGiven.replace("search","")
        speak(f"TED is searching the web for the query...")
        webbrowser.open(queryGiven)

    elif 'open command prompt' in queryGiven:
        os.system("Start cmd")

    elif "who made you" in queryGiven or "who created you" in queryGiven: 
        speak("TED was developed by Shreyas")

    elif 'hello' in queryGiven:
        speak(f"Hi {uName}!")

    elif 'stop listening' in queryGiven or 'stop' in queryGiven:
        speak("TED is halting it's operations now. Bye bye!")
        exit()
    
    else:
        speak(f"Sorry {uName}, TED finds the command too complex.. Please wait for the updates..")

