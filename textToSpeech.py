from subprocess import call
import time
a = "hello dear"

def mySpeechMale(text):
    call(["espeak","-s140 -ven+18 -z",text])
    return None

def mySpeechFemale(text):
    call(["espeak","-s130 ","-ven+m1",text])
    return None

"""
if __name__=="__main__":
    mySpeechFemale(a)
    time.sleep(1)
    mySpeechMale(a)
"""
    
"""
import subprocess, signal, time
proc = subprocess.Popen("./wait")

def voice(text):


    proc = subprocess.Popen(["espeak","-s140 -ven+18 -z",text])

    proc.send_signal(signal.SIGINT)    

"""