import RPi.GPIO as GPIO
import time
from control import face, objects, read
from textToSpeech import mySpeechMale

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


while True:
    if GPIO.input(31)==GPIO.HIGH:
        mySpeechMale("face detection")
        print("31  for face" )
        face()

    elif GPIO.input(33)==GPIO.HIGH:
        mySpeechMale("text detection")
        print("33 for read")
        read()

    elif GPIO.input(35)==GPIO.HIGH:
        mySpeechMale("object detection")
        print("35 objects")
        objects()

    elif GPIO.input(37)==GPIO.HIGH:
        print("button pressed at 37")

    else:
        print("no input")