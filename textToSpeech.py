from subprocess import call

a = "hello dear"

def my_speech(text):
    call(["espeak","-s140 -ven+18 -z",text])

