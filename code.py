# importing libraries
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import pywhatkit as wk
import os
import cv2
import sys
import time
import pyautogui as pi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voice[1].id')
engine.setProperty('rate',150)

# functions
def speak(audio) : 
    engine.say(audio)
    engine.runAndWait()

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source : 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said : {query}\n")
    except Exception as e :
        print("Say that gain please...")
        return "None"
    return query

def WishMe() :
    hour = datetime.datetime.now().hour

    if hour>=0 and hour<12 : 
        speak("Good morning!")
    elif hour>=12 and hour<18 :
        speak("good afternoon")
    else :
        speak("good evening")
    speak("What can I do for you today?")


# main function
if __name__ =="__main__" :
    WishMe()

    while True :
        query = takeCommand().lower()

        if "type" in query :
            query = query.replace("type","")
            pi.typewrite(f"{query}" , 0.2)

        elif "rio" in query :
            print("Yes, How may I help you?")
            speak("Yes, How may I help you?")

        elif "introduce yourself" in query :
            print("Hello everyone , My name is Rio . I am a virtual Desktop Assisstant. I can do various tasks like : searching information on web and wikipedia , opening applications , searching on YouTube and whatever my creator programmed me to do.")
            speak("Hello everyone , My name is Rio . I am a virtual Desktop Assisstant. I can do various tasks like : searching information on web and wikipedia , opening applications , searching on YouTube and whatever my creator programmed me to do.")

        elif "job"  in query :
            print("I appreciate you like my work.")
            speak("I appreciate you like my work.")

        elif "who are you" in query :
            print("Hi!I am your rio")
            speak("Hi!I am your rio")

        elif "who created you" in query :
            print("Miss Vanshika")
            speak("Miss Vanshika")

        elif "what are the things you can do" in query :
            print("I would love to help you. I can do various tasks like : searching information on web and wikipedia , opening applications , searching on YouTube and whatever my creator programmed me to do")
            speak("I would love to help you. I can do various tasks like : searching information on web and wikipedia , opening applications , searching on YouTube and whatever my creator programmed me to do")

        elif "what is" in query : #1
            speak("Searching web resources. kindly wait")
            query = query.replace('what is','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who is" in query : #2
            speak("Searching web resources. kindly wait")
            query = query.replace('who is','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "just open google" in query : #3
            webbrowser.open("google.com")

        elif "open google" in query : #4
            speak("Do you want me to search anything on google?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry,sentences=2)
            print(results)
            speak(results)

        elif "just open youtube" in query : #5
            webbrowser.open("youtube.com")

        elif "open youtube" in query : #6
            speak("Do you want me to search anything on youtube?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif "search on youtube" in query : #7
            webbrowser.open("youtube.com")
            query = query.replace('search on youtube','')
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif "incorrect query" in query : #8
            speak("Please be more clearer")

        elif "close browser" in query : #9
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query : #10
            os.system("taskkill /f /im chrome.exe")

        elif "romantic music on spotify" in query : #11
            webbrowser.open("https://open.spotify.com/playlist/3aD78p7nhLiKAqFMN03t0J")
            time.sleep(10)
            pi.press(x=520,y=603,clicks = 1)

        elif "stop playing" in query : 
            speak("As you say")
            time.sleep(2)
            pi.click(x=519,y=602,clicks =1)

        elif "open command prompt" in query : #12
            os.system("start cmd")

        elif "close chrome" in query : #13
            os.system("taskkill /f /im cmd.exe")

            
        elif "whats the time" in query : #14
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Time is {strTime}")

        elif "shutdown my system" in query : #15
            os.system("shutdown /s /t S")

        elif "lock my system" in query : #16
            os.system("rundll32.exe powerprof .dll,SetSuspendState 0,1,0")

        elif "go to sleep" in query : #17
            speak("alright , i am switching off")
            sys.exit()

        elif "open camera" in query : #18
            cap = cv2.VideoCapture(0)
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                    break
                cap.release()
                cv2.destroyAllWindows()

        elif "screenshot" in query : #19
            speak("okay, please Tell me the name of your ss file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pi.screenshot()
            img.save("f{name}.png")
            speak("Screenshot saved")

        elif "my ip address" in query : #20
            speak("checking your ip address")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip address is ")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak , please try again after some time")

        elif "volume up by" in query : #2 up  #21
            query = query.replace("volume up by ","")
            i=0
            while i!=(int(query)/2):
                pi.press("volumeup")
                i=i+1

        elif "volume down by" in query : #2 down  #22
            query = query.replace("volume down by ","")
            i=0
            while i!=(int(query)/2):
                pi.press("volumedown")
                i=i+1

        elif "mute" in query :  #23
            pi.press("volumemute")

        elif "copy this" in query : #24
            pi.keyDown("ctrl")
            pi.press("c")
            pi.keyUp("ctrl")

        elif "open start" in query : #25
            pi.press("start")

        elif "select all" in query : #26
            pi.keyDown("ctrl")
            pi.press("a")
            pi.keyUp("ctrl")

        elif "open task manager" in query : #27
            pi.hotkey('ctrl' ,'shift','esc')

        elif "open search bar" in query : #28
            pi.press('win')

        elif "open notepad" in query : #29
            pi.press('win')
            time.sleep(1)
            pi.write('notepad')
            time.sleep(1)
            pi.press('enter')
           
        elif "write on notepad" in query : #30
            query = query.replace('write on notepad','')
            pi.press('win')
            time.sleep(2)
            pi.typewrite('notepad',0.5)
            pi.press('enter')
            time.sleep(2)
            pi.typewrite(f"{query}",0.2)

        elif "open app" in query : #31
            query = query.replace("open app","")
            pi.hotkey('win')
            time.sleep(0.7)
            pi.write(f"{query}")
            pi.press("enter")

        elif "close" in query :
            pi.click(x=1886,y=14,clicks=1)

        elif "bye" in query :
            speak("Hope you loved my work")
            
