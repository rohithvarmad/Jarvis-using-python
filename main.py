import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say("hello my name is jarvis")
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')

    except:
        pass
    return command


def run_jarvis():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("current time is "+time)
    elif 'search about' in command:
        person=command.replace("search about",'')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk("I dont understand u can u repeat it again")

while True:
    run_jarvis()