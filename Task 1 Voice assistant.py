import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:  # Adjust device_index based on your setup
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't get that. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"

    return query.lower()

def sendEmail(to, content):
    # Add your email configuration here
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'kayarkarhemangi@gmail.com'
    smtp_password = 'hemangi@448'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to, content)
        server.close()
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

if __name___ == "_main_": wish_me() 
speak("Hi Hemangi, how are you? My name is Spark. I am a Desktop Assistant. How may I help you?")
    
while True:
        query = takeCommand()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.DisambiguationError as e:
                print(f"Ambiguous query. {e}")
                speak("I found multiple results. Please be more specific.")
            except wikipedia.PageError as e:
                print(f"Page not found. {e}")
                speak("I couldn't find any information on this topic.")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open Chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")
        elif 'play music' in query:
            music_dir = "https://www.youtube.com/watch?v=8kxufj_snhI&ab_channel=T-Series"
            songs = os.listdir(music_dir)
            print(songs)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                print("No songs found in the specified directory.")
                speak("No songs found in the specified directory.")
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        elif 'open code' in query:
            code_path = "c:\\Users\\kayar\\Desktop\\sky.py"
            os.startfile(code_path)
        elif 'email to Hemangi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kayarkarhemangi@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")