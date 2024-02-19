import speech_recognition as sr #rozpoznawanie głosu
import time
import pyautogui as pg
import pyttsx3 as tts #tworzenie głosu bota
#PyAudio and Interned connection required


r = sr.Recognizer()
engine = tts.init() #inicjalizacja silnika zmiany tekstu na mowę
engine.setProperty('rate', 200)

def say():
    engine.say("Słucham")
    engine.runAndWait()

def get_text():
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            say()
            print("    Nasłuchuje...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='pl-PL')
            print("    ...Koniec nasłuchiwania")
            if text !="":
                return text
            return 0
        except:
            print("    ...Koniec nasłuchiwania")
            return 0

while True:
    try:
        txt = get_text().lower()
        print(txt)

        if "koniec" in txt:
            break
        elif "sprawdz" in txt:
            pg.press('enter')
        elif "źle" in txt or "słab" in txt:
            pg.press('1')
        elif "średn" in txt:
            pg.press('2')
        elif "świetn" in txt:
            pg.press('3')
        time.sleep(1.5)

    except:
        time.sleep(0.5)