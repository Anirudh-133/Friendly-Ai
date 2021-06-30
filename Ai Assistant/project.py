import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning! ")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am donald trumph sir, please  tell your command")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening....")
       r.pause_threshold = 1
       audio =r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")   

    except Exception as e:
        
        print("Say that again please....")
        speak("say that again")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com,587')
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email,to,content')
    server.close()



if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
    
      query=takeCommand().lower()

      if 'wikipedia' in query:
          speak('searching in Wikipedia...')
          results=wikipedia.summary(query,sentences=1)
          speak("Wikipedia says")
          print(results)
          speak(results)
          
      elif 'open youtube' in query:
          # elif 'youtube' in query:      #To directly open ytube
          # webbrowser.open("youtube.com")
           speak("what you want to search")
           cm1=takeCommand().lower()
           webbrowser.open("https://www.youtube.com/results?search_query="+cm1)
      elif 'open google' in query:
           speak("what you want to search")
           cm=takeCommand().lower()
           webbrowser.open(f"{cm}")
      elif'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir,the time is {strTime}")

      elif 'email to paimon' in query:
            try:
                speak("what should i send?")
                content=takeCommand()
                to="singhanirudh975@gmail.com"
                sendEmail(to,contact)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Im not able to send")
      elif 'send message' in query:
            speak("message is sending")
            kit.sendwhatmsg("+918083290955","Apun trumph hai",17,20)
      elif 'shutdown' in query:
            speak("bye bye sir")
            sys.exit()
      elif 'smart boy':
            speak("thank you sir")


            
      

        