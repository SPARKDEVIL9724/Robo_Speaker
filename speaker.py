import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

def robospkr(message:str):
    speak.Speak(message)

if __name__=="__main__":
    while True:
        text =input("Enter What to say ")
        if text=="qt":
            robospkr("Thank You")
            robospkr("Bye Bye")
            break
        else:
            robospkr(text)
