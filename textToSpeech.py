import pyttsx3

red =open('textf.txt','r+') 
a = red.read()

def my_speech(my_message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    engine.say('{}'.format(my_message))
    engine.runAndWait()
    #rate = engine.getProperty('rate')


my_speech(a)