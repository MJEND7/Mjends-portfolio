import pyttsx3
import datetime
import sys
import smtplib
import random
import webbrowser
import subprocess
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import time
import random,os
import sys



engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('36Y6YU-PJQ6Y53RQR')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-4].id)

def speak(audio):
    print('mendicant bias: ' + audio)
    engine.say(audio)
    engine.runAndWait()


    



speak('')
speak(' ready sir')




def myCommand():

    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))


    return query



if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'are you online fri 01' in query :
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 0 and currentH < 12:
              speak('yes and Good Morning!')

            if currentH >= 12 and currentH < 18:
              speak('yes and Good Afternoon!')

            if currentH >= 18 and currentH !=0:
              speak('yes and Good Evening!')
 
        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
            
        elif 'fortnite tips and tricks' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/results?search_query=fortnite+tips+and+tricks')
                
        elif 'halo tips and tricks' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/results?search_query=halo%20tips%20and%20tricks&pbjreload=10')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open my drive' in query:
             speak('okay')
             webbrowser.open('https://drive.google.com/drive/my-drive')

        elif 'open steam' in query:
            speak('okay')
            webbrowser.open('https://store.steampowered.com/')
                   
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

            
        elif 'tech news' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/channel/UCeeFfhMcJa1kjtfZAGskOCA')
        
        elif "what is your name" in query or 'who are you' in query or 'your name' in query:
            stMsgs = ['friday', 'my name is friday']
            speak(random.choice(stMsgs))

        elif "hi" in query or 'hello' in query:
            stMsgs = ['hi', 'hello', 'how are you','hi','hello','how are you','hi','hello','hi']
            speak(random.choice(stMsgs))
            
        
        elif "you are mean" in query:
            stMsgs = ['you are a meme','so sorry']
            speak(random.choice(stMsgs))
        elif "that is ok" in query:
            stMsgs = ['ya sorry','i am sad ']
            speak(random.choice(stMsgs))
            
        elif "sleep" in query:
             time.sleep(60)
             speak('ready')
        elif "you are wrong" in query:
             speak ("are you doubting my capability well then you can do this with out me shutting down 1.......2........3...... ")
             sys.exit()

        elif "hi do not like you" in query or 'i hate you' in query   :
             speak ("well i hate you so eat. yeet. dot. exe. file.")
             music_folder = "C:/Users/marku/Music/" 
             music = ["yeet.exe"]
             random_music = music_folder + random.choice(music) + '.mp3'
             os.system(random_music)
             sys.exit()
             
        elif "game sleep" in query:
             time.sleep(30)

        elif "loop" in query:
           os.spawn("‪E:\VoidLauncher.exe")
           
             
             
        elif "help me with the game" in query:
             stMsgs = ['Use the noob combo (Plasma Pistol and Battle Rifle), use power weapons, and exploit every aspect of the game. Some combos such as Magnum+SMG are suited for close range. Single weapons such as the Battle Rifle and Sniper Rifle are long range weapons.', 'Some players love to hide behind corners and remain crouched. Others have the analog stick pushed to the edge the entire game. Both styles have pros and cons. Try them.', 'Talk with your team. Even chit-chat is useful for goading them into useful communication. Report every enemy sighting and keep your ears open to weapon locations.', 'Play plenty of fun games but always try to improve your skills. Skills such as aiming and moving may seem simple but make all the difference in the', 'Learn the weapons, starting with the Battle Rifle. Halo has a lot of weapons, and the more you know about them better you will be in any mode. The essential weapon to learn is the battle rifle, which shoots accurate, 3-bullet bursts suitable for a variety of distances. With proper shot placement (the head), it can take down most enemies in a few hits, and the scope greatly increases your range. The Covenant Carbine is a similar weapon, though slightly less common. As you improve, you can move on to other weapons for more specific scenariosPistols are really only useful when duel wielded, or against weak enemies when you want to conserve ammunition.Rifles, Needlers, SMG are fast-shooting damage dealers used in mid to close range fights. Usually, you need to duel-wield them to be effective.Sniper Rifles are essential for a good Halo player. They can kill most enemies with a single shot to the head, and are highly accurate.Shotguns and swords are only good for close-range, quick kills. You need to be very close to the enemy for them to be effective, but they kill quickly.']
             speak(random.choice(stMsgs))

             
             
        elif "give me a heads up" in query or 'help!!' in query:
            stMsgs = ['Try playing without shields; it makes it harder and you will get better.', 'Use weapons that have small aiming reticles, Ex.Battle Rifle or Sniper. Your aiming skills will improve a lot.', 'Find out what you did wrong after a death, or a game.', 'Use grenades to start and finish fights -- pulling someone out of cover or getting the kill as they run away', 'Strafing needs to be side to side moving forwards and backward barely changes your opponents target ' ]
            speak(random.choice(stMsgs))

        elif "shut my pc down" in query:
            speak('ok sir')
            os.system('shutdown -s')
            
        elif "flower" in query:
            speak('ok sir')
            os.system('E:\all')          
            
        elif "do a weather check" in query or 'weather check' in query or 'weather' in query:
            speak('yes sir')
            webbrowser.open('http://www.bom.gov.au/australia/meteye/')

        elif "wold map" in query or 'map' in query or 'earth map' in query:
            speak('yes sir')
            webbrowser.open('https://www.google.com/maps/@-17.3293473,135.8748405,7886500m/data=!3m1!1e3')
               
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('markuss.cowburn@gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("YEETBOT", '125my52l')
                    server.sendmail('Your_Username', "me", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'computer' in query:
            speak('Hello Sir')

       

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query or 'drop the pin' in query:
            music_folder = "C:/Users/marku/Music/" 
            music = ["untitled", "untitled10", "untitled9", "lasagna", "untitled4","untitled7"]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')
            time.sleep(145)
            speak('ready')

        

        
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('')
                    speak('')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('')
                    speak('')
                    speak(results)

            except:
                webbrowser.open('')

        
        speak('')
