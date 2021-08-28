import pyttsx3 #text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('Initializing Black ...')

MASTER = 'Edwin'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning' + MASTER)
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon' + MASTER)
    else:
        speak('Good Evening', MASTER)
        speak('')

# microphone
def takeCommand():
    r = sr.Recognizer()
    # My Microphone System Name
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('Listening ...')
        audio = r.listen(source)

    try:
        print('Recognizing ...')
        query = r.recognize_google(audio, language='en-us')
        print(f"You Said : {query} \n")
    except Exception as e:
        print('Say That Again Please ...')
        query = None
    return query

# main
speak('Hello my name is Black, Can i help you ?')
wishMe()
query = takeCommand()

# logic for tasks as per query
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia ...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    url = 'youtube.com'
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\ASUS\\Videos\\Spotify"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")