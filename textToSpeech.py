from subprocess import call
import time
a = "hello dear"

def mySpeechMale(text):
    call(["espeak","-s140 -ven+18 -z",text])
    return text

