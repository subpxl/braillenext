from subprocess import call
import time
a = "hello dear"

def mySpeechMale(text):
    call(["espeak","-s140 -ven+18 -z",text])

<<<<<<< HEAD



=======
def mySpeechFemale(text):
    call(["espeak","-s160 ","-ven+f1",text])



if __name__=="__main__":
    mySpeechFemale(a)
    time.sleep(1)
    mySpeechMale(a)

>>>>>>> night 10 august
    
"""
import subprocess, signal, time
proc = subprocess.Popen("./wait")

def voice(text):


    proc = subprocess.Popen(["espeak","-s140 -ven+18 -z",text])

    proc.send_signal(signal.SIGINT)    

"""