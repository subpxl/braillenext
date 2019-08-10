from subprocess import call

a = "hello dear"

def my_speech(text):
    call(["espeak","-s140 -ven+18 -z",text])




    
"""
import subprocess, signal, time
proc = subprocess.Popen("./wait")

def voice(text):


    proc = subprocess.Popen(["espeak","-s140 -ven+18 -z",text])

    proc.send_signal(signal.SIGINT)    

"""