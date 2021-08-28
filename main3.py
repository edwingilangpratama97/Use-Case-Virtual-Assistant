from settings import *
from time import ctime # time detials
from  PIL import Image
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
import pyautogui
import urllib.request
import bs4 as bs #Beautiful Soup is a library that makes it easy to scrape information from web pages. 


listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(): 
    global command  
    try:
        with sr.Microphone() as source:
            print(f'{ASSISTANT_NAME} : Listening ...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
        
    except sr.RequestError:
        print('Sorry, my speech service is down')
        talk('Sorry, my speech service is down')

    except:
        pass
        # command = None

    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print(f"{ASSISTANT_NAME} : Hello Good Morning {MASTER_NAME}")
        talk("Hello Good Morning" + MASTER_NAME)
    elif hour >= 12 and hour < 18:
        print(f"{ASSISTANT_NAME} : Hello Good Afternoon {MASTER_NAME}")
        talk("Hello Good Afternoon" + MASTER_NAME)
    else:
        print(f"{ASSISTANT_NAME} : Hello Good Evening {MASTER_NAME}")
        talk("Hello Good Evening" + MASTER_NAME)

def there_exists(terms):
    for term in terms:
        if term in command:
            return True

def run():
    command = take_command()
    print(f'{MASTER_NAME} :', command)

    # 1) if got greeting
    if there_exists(['hey','hi','hola','hello','wassup',]):
        greetings=[f"Hi sir, What we gonna do today {MASTER_NAME} ?" , f"Hi sir, what are we doing today {MASTER_NAME} ?" , f"Hi sir, How can i help you {MASTER_NAME} ?"]
        sentence=greetings[random.randint(0,len(greetings)-1)]
        print(f'{ASSISTANT_NAME} : {sentence}')
        talk(sentence)

    #2))name
    elif there_exists(["what is your name","what's your name","tell me your name"]):
        sentence = f"My name is {ASSISTANT_NAME}, You can call me {ASSISTANT_NAME}"
        print(f'{ASSISTANT_NAME} : {sentence}')
        talk(sentence)

    #3)) greeting
    elif there_exists(["how are you","hoe are you","how are you doing"]):
        sentence = "I m very well sir, how are you? thanks for asking"
        print(f'{ASSISTANT_NAME} : {sentence}')
        talk(sentence)
        
    #4))time
    elif there_exists(["whats the time","tell me the time","what time is it"]):
        time = datetime.datetime.now().strftime('%I:%m %p')
        sentence = f"Current time is {time}"
        print(f'{ASSISTANT_NAME} : {sentence}')
        talk(sentence)

    #5))search google
    elif there_exists(["search for"]) and 'youtube' not in command:
        search_term=command.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        talk("Her is what i found for"+search_term + "on google")
        
    #6))) search youtube
    elif there_exists(["search for youtube for","youtube"]):
        search_term=command.split("for")[-1]
        print(search_term)
        url="https://www.youtube.com/results?search_query="+ search_term
        webbrowser.get().open(url)
        talk("Here is what i found for "+ search_term + "on youtube")
        
    #7))) get to know the weather
    elif there_exists(["weather","how the weather outside","Please get the report of waether"]):
        search_term=command.split("for")[-1]
        url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)#opens the webrowser
        talk("Here is your report sir")
    
    #8)) get to know stock price
    elif there_exists(["price of"]):
        search_term=command.split("for")[-1]
        url="https://google.com/search?q="+ search_term
        webbrowser.get().open(url)
        talk("Here is what i found for"+ search_term)
    
    #9 get to listen music
    # elif there_exists("play spotify music"):
    #     search_term=command.split("for")[-1]
    #     url="https://open.spotify.com/search/"+search_term
    #     webbrowser.get().open(url)
    #     talk("Enjoy sir")

    #10 screenshot
    elif there_exists(["capture","my screen","screenshot"]):
        myScreenshot=pyautogui.screenshot()
        myScreenshot.save('image.png')

    #11 calc
    elif there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = command.split()[1]

        if opr == '+':
            talk(int(command.split()[0]) + int(command.split()[2]))
        elif opr == '-':
            talk(int(command.split()[0]) - int(command.split()[2]))
        elif opr == 'multiply' or opr == '*':
            talk(int(command.split()[0]) * int(command.split()[2]))
        elif opr == 'divide' or opr == '/':
            talk(int(command.split()[0]) / int(command.split()[2]))
        elif opr == 'power' or opr == '**':
            talk(int(command.split()[0]) ** int(command.split()[2]))
        else:
            talk("Wrong Operator")

    #12 direct play youtube
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print(f'{ASSISTANT_NAME} : Playing {song}')
        pywhatkit.playonyt(song)

    #13 map 
    elif 'map' in command:
        location = command.replace('map', '')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print(f'{ASSISTANT_NAME} : Here is the map of {location}')
        talk('Here is the map of ' + location)

    #14 wikipedia
    elif 'tell me about' in command:
        ask = command.replace('tell me about', '')
        info = wikipedia.summary(ask, sentences=2)
        print(f'{ASSISTANT_NAME} : {info}')
        talk(info)

    #15 joke
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(f'{ASSISTANT_NAME} : {joke}')
        talk(joke)

    #16 asking 
    elif 'who are you' in command:
        print(f'{ASSISTANT_NAME} : I am {ASSISTANT_NAME}. Your 24 7 virtual assistant. if you are bored i can tell you a joke, i can play youtube videos for you, and blah blah and i am awesome.')
        talk(f'I am {ASSISTANT_NAME}. Your 24 7 virtual assistant. if you are bored i can tell you a joke, i can play youtube videos for you, and blah blah and i am awesome.')

    #17 thank you
    elif 'thank you' in command:
        print(f'{ASSISTANT_NAME} : Your welcome. Anything else you want me to do {MASTER_NAME} ?')
        talk(f'Your welcome. Anything else you want me to do {MASTER_NAME} ?')

    #18 for exit       
    elif there_exists(["exit","goodbye","quit","take some rest bro"]):
        print(f'{ASSISTANT_NAME} : We could continue more {MASTER_NAME}, well goodbye')
        talk(f"We could continue more {MASTER_NAME}, well goodbye")
        exit()

    else:
        print(f'{ASSISTANT_NAME} : Sorry, I did not get that')
        talk('Sorry, I did not get that')


if __name__ == '__main__':
    wishMe()
    print(f'{ASSISTANT_NAME} : I am {ASSISTANT_NAME}, Can i help you {MASTER_NAME}?')
    talk(f'I am {ASSISTANT_NAME}, Can i help you {MASTER_NAME}?')
    while True:     
        run()