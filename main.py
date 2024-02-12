import speech_recognition as sr
import time
import pyautogui as pg
#PyAudio required

r = sr.Recognizer()

def get_text():
    with sr.Microphone() as source:
        try:
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
        txt = get_text().lower().split()
        if txt == 0:
            raise Exception(0)
        print(txt)

        if txt[0] == "koniec":
            break
        elif txt[0] == "sprawdzam":
            pg.press('enter')
        elif txt[0] == "źle":
            pg.press('1')
        elif txt[0]=="średnio":
            pg.press('2')
        elif txt[0]=="świetnie":
            pg.press('3')
        time.sleep(2)
    except:
        pass