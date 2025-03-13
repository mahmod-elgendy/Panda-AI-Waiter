import pandas as pd
from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3

df = pd.read_csv("Panda_Dataset - Sheet1.csv")

def speak(text):
    audio_file = "response.mp3"
    # Delete the previous audio file if it exists
    if os.path.exists(audio_file):
        os.remove(audio_file)
    # Generate and save new speech
    tts = gTTS(text=text, lang="ar")
    tts.save(audio_file)
    
    # Play the new audio file
    playsound(audio_file)



def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("تحدث الآن...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="ar")
            print("أنت قلت: ", text)
            return text.lower()
        except sr.UnknownValueError:
            print("لم أتمكن من فهم ما قلته.")
            return ""
        except sr.RequestError:
            print("خطأ في الاتصال بخدمة التعرف على الصوت.")
            return ""

def chatbot(df):
    while True:
        user_input = user_input = listen()
        if not user_input:
            continue
        
        if user_input == "سلام" or user_input == "باى" or user_input == "مع السلامه" or user_input == "خلاص شكرا" or user_input == "ميرسى" or user_input == "اشكرك":
            response = "الوداااع"
            print(response)
            speak(response)
            break


        
        response = None
        
        for index, row in df.iterrows():
            if row["KEYWORD"] in user_input:
                response = row["RESPONSE"]
                break
        
        if response:
            print(response)
            speak(response)
        else:
            print("سوري مفهمتش, ممكن تعلمني؟")
            speak("سوري مفهمتش, ممكن تعلمني؟")

            new_response = input("ايه الرد المطلوب: ")

            df.loc[len(df)] = {"KEYWORD": user_input, "RESPONSE": new_response} 
            print("ميرسي كتير")
            speak("ميرسي كتير")

chatbot(df)
