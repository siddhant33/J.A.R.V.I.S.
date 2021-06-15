import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import time
import pyjokes
import pyautogui
import subprocess

MASTER = "sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!" +MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+MASTER)   

    else:
        speak("Good Evening!" +
        MASTER)  

    speak("Iam Jarvis.. Please tell me how may I help you") 

def takecommand():
    

    r = sr.Recognizer()
    my_mic = sr.Microphone(device_index=1)
    with my_mic as source:

        print("listening...")
        r.pause_threshold = 1             
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query     


if __name__ == "__main__":
    wishMe()
    takecommand()

############## #main function###########################################
    while True:
        query = takecommand().lower()
# All the commands said by user will be 
		# stored here in 'query' and will be
		# converted to lower case for easily 
		# recognition of command        
        # Logic for executing tasks based on query
        if 'tell me' in query or "who" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to me")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")

        elif'check gmail' in query:
            speak("ok sir.")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")    


        elif'open chrome'in query:
            speak("opening chrome")
            webbrowser.open("https://www.google.co.in/")

        elif 'open sweet memory channel' in query:
            speak("opening channel")
            webbrowser.open("https://www.youtube.com/channel/UCP2BnrfqXMURueZdI7H9ioA")


        elif 'open my channel' in query:
            speak("opening channel")
            webbrowser.open("https://www.youtube.com/channel/UC9O_bcJ5Q8EI-aWkE5DY9pw/videos")    
          

        elif 'open google' in query:
            speak("opening google. sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
           
        elif 'open facebook' in query or 'any facebook messages' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/siddhant.thakur.5074/") 
            speak("looks like you are all caught up sir!")  

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")   

        elif"open cmd" in query:
            speak("ok sir.")
            os.system("start cmd")   


        elif'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir") 

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif'do you know me' in query:
            speak("If you talk then definately your human.") 

        elif'why you came to world' in query:
            speak("I was created as a Minor project by Siddhant")
            speak("further It's a secret")    

#to close it
        elif"close cmd" in query:
            speak("ok sir.")
            os.system("taskkill /f /im cmd.exe")

        elif"close it" in query:
            speak("ok sir.")
            os.system("taskkill /f /im chrome.exe")

#play music
        elif 'play music' in query or 'hit some music' in query:
            music_dir = 'C:\\Users\\computer\\Desktop\\personal\\music\Audio'
            songs = os.listdir(music_dir)
            speak(" would you like this .")
            #print(songs)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, rd))
         
        elif 'next music' in query or "next" in query:
            music_dir = 'C:\\Users\\computer\\Desktop\\personal\\music\Audio'
            songs = os.listdir(music_dir)
            #print(songs)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, rd))  

        elif'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif 'something popular' in query:
            speak("okay. changing it to a popular song!")
            music_dir = 'C:\\Users\\computer\\Desktop\\personal\\test'
            songs = os.listdir(music_dir)
            #print(songs)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, rd))

        elif'intense' in query:
            speak("ooh, should i play any Romantic songs")     
            
#to stop music
        elif"stop music" in query or 'stop' in query:
            speak("ok sir")
            os.system("taskkill /f /im vlc.exe")
            speak("then what do you want me to play, sir")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"Sir, the time is {strTime}")
            speak("and you are working since 3 am. i think you have to take a rest.")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif"say something" in query:
            speak("please subscribe the channel, and press the bell icon. so you will never miss latest update")    

        elif"hello jarvis" in query:
            speak("Now may i introduce myself. I am jarvis. Just A Rather Very Intelligent System. And i am  here to asset you with a verity of task as best i can. 24 hours a day and 7 days a week. im always be there ")


#quit program             

        elif'you can sleep now' in query or"take a rest"in query :
            speak("ok sir , have a good day ")
            os.system("taskkill /f /im code.exe")
            sys.exit() 
#to set alerm
        elif "set alarm" in query:
            rn = str(datetime.datetime.now().time())
            print(rn)
            if rn==22:
                music_dir = 'C:\\Users\\computer\\Desktop\\personal\\music\Audio'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

#for jokes                
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
#switch window
        elif"switch the window" in query or 'wake up' in query:
            speak("ok sir.")
            pyautogui.keyDown("Alt")
            pyautogui.press("Tab")
            time.sleep(1)
            pyautogui.keyUp("Alt")

        elif'check messages' in query or 'any messages' in query:
            speak("ok sir, wait a minute. im checking messages")
            pyautogui.press("down",presses=80)
            speak("No sir, you didnt recevied any messages")
            pyautogui.press("up",presses=40)    

        elif"scroll down" in query or "down" in query:
            speak("scrolling")
            pyautogui.press("down", presses=30)

        elif'scroll up' in query:
            speak("scrolling")
            pyautogui.press("up", presses=15)    
            



#to take a screeenshot                                                                                       
        elif"take screenshot" in query or "take a screenshot" in query:
            speak("sir , please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few second , i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("done sir , the screenshot is saved in our main folder . now i am ready for another task")

       