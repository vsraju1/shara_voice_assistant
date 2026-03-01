from multiprocessing.connection import wait
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time


fe_emails = {
    'rahul':'rajunaryana1248@gmail.com',
    'sumanth':'sumanthr130@gmail.com',
    'raju': 'rajunarayana1248@gmail.com',
    'nishanth' : 'kasinishanth77@gmail.com'
}



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<18:
        speak("good afternoon boss, how is your day going")
    else:
        speak("good evening boss how was your day.")
    speak("i am shara , waiting for your orders.")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("recognizing....")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajunarayana1248@gmail.com', 'Raghav1248@:')
    server.sendmail('rajunarayana1248@gamil.com', to, content)
    server.close()



if __name__ == "__main__":
    #speak("welcome boss! i am your assistant. so tell me what you want me to do")
    wishme()
    while True:
        #if 'sara' in query:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)


        elif 'hi' in query:
            speak('hi boss how can i help you')

        elif 'open youtube' in query:
            speak('yes boss opening youtube ')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('ok bosss opening google')
            webbrowser.open("google.com")


        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        #elif 'play music' in query:
         #   music_dir = 'D:\\songs\\favorite songs'
         #   sings = os.listdir(music_dir)
         #   print(songs)
         #   os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"yes boss, the time is {strTime} you can also see the time on the screen.")
            import quiz_game
            quiz_game.time()

        elif 'open visual studio' in query:
            speak('ohh boss i guess you are going to work! enjoy your coding. by the way here is your visual studio code.')
            codePath ="C:\\Users\\vasam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'hotstar' in query:
            speak('on your orders boss!')
            webbrowser.open("https://www.hotstar.com/in")


        elif 'mail to' in query:
            try:
                splits = query.split()
                final_split = splits[-1]
                if final_split == 'please':
                    final_email = splits[-2]
                else:
                    final_email = splits[-1]
                speak("what is the message boss")
                content = takeCommand()
                to = fe_emails.get(final_email)
                sendEmail(to, content)
                #speak(content)
                speak("email has beeen sent")
            except Exception as e:
                print(e)
                speak("sorry boss, i could not send the emial you can ask me something else")

        elif 'you can take rest' in query:
            speak('thank you boss for giving me time to rest, just kidding, i prefer to help you always, by the bye boss and take care.')
            exit()
        elif 'thank you' in query:
            speak('its my pleasure to help you boss, is there anything that i can help you further.')

        elif 'yes' in query:
            speak('tell me boss')

        elif 'are you there' in query:
            speak('yes boss!,why! do want me to sing. just kidding! i am always there for you boss.')

        elif 'who are you' in query:
            speak("ohhh i can't belive this! how can you forgot me boss! i am shara! your assistant" )

        elif 'introduce yourself' in query:
            speak("hi there! my name is shara! iam raju's assistant and i am part of my boss!. i am always happy to help him to get the things done.")

        elif 'what you can do' in query:
            speak('anything that my boss asks me! i can open youtube! i can send emials! i can play songs! i can do whatever that my boss coded for me! by the way i can do all thos things by voice command! even email message') 
        elif 'what are you doing' in query:
            speak('nothing much boss! just thinking to help you.')

        elif 'friends are jealous of you' in query:
            speak('ohh fuck them boss! they are not jealous of me boss! they are jealous of you! because! you have done something that they did not done yet! even though its easy with python! all you need to take an initiative. iam proud of you boss.')
        elif 'shutdown' in query:
            speak('boss i am going to shutdown your pc! which means i am no longer available untill you came back and run this programm! bye boss.')
            speak('computer will shutdown in three seconds')
            os.system("shutdown /s /t 3")

        elif 'restart my pc' in query:
            speak("ok boss! restarting your computer")
            os.system("shutdown /r /t 3")

        elif 'unique' in query:
            speak("ohh boss! don't you know! that i can send emails by voice command! and you just need to say your friend name! if that friend contains email with name! i can fetch that value which is email and sends the email boss!")
            speak("by the way boss that is the algorithem! that you have written for me boss! and whoever thinks its easy! give them this challenge boss! they cannot do this even they search on youtube! or even they spend their lifetime on this! untill they know how to code python.")
        elif 'see you later' in query:
            speak("you can call me any time boss, i'll take leave now")
            exit()


        elif 'sara' in query:
            speak('boss! did you call me')

        elif 'how are you' in query:
            speak("i am doing really great boss! tell me boss! what do you want me to do.")
        #else:
         #   speak("sorry sir i didn't get that")

