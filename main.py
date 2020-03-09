
from objectdetect import ObjectDetect, TextDetect
import serial
from gpiozero import Button
from signal import pause
import subprocess
import time
import os
import picamera

#subprocess.Popen(['sudo','pkill','rfcomm'])
subprocess.Popen(['sudo','rfcomm','watch','hci0'])


camera = picamera.PiCamera()
imgpath = "/home/pi/cashma/test/testimages/sample.jpg"

def capture():
    i = 0
    i =i+1
    camera.capture(imgpath)
    return imgpath


ser = serial.Serial('/dev/rfcomm0')

text_button = Button(19)
object_button = Button(26)
location_buton = Button(6)
emergency_button = Button(13)

inst = ObjectDetect()

textInst = TextDetect()
str2 = ("the content is ").encode()



def obj_func():
    str1 = ("detecting please wait").encode()
    print(str1)
    ser.write(str1)
    str3 = inst.localize_objects(capture()).encode()
    ser.write(str2)
    ser.write(str3)
    print("The values are %s AND %s" % (str3, str2))

def text_func():
    str1 = ("reading please wait").encode()
    print(str1)
    ser.write(str1)
    str3 = textInst.text_within(capture()).encode()
    print("The values are %s AND %s" % (str3, str2))
    ser.write(str3)
    ser.write(str2)

def location_func():

    ser.write(("#locationAsk").encode())

def emergency_func():
    ser.write(("#emergencyAsk").encode())


# when the button is pressed
text_button.when_pressed = text_func
object_button.when_pressed = obj_func
location_buton.when_pressed = location_func
emergency_button.when_pressed = emergency_func

pause()


