
from objectdetect import ObjectDetect, TextDetect
import serial
from gpiozero import Button
from signal import pause
import subprocess
import time
import os
import picamera
from gpiozero import LED
from time import sleep

#subprocess.Popen(['sudo','pkill','rfcomm'])
#subprocess.Popen(['sudo','rfcomm','watch','hci0'])



imgpath = "/home/pi/cashma/test/testimages/sample.jpg"
ser = serial.Serial('/dev/rfcomm0')

welcome = (" the machine is connected").encode()

print(welcome)
ser.write(welcome)

str2 = ("the content is ").encode()



camera = picamera.PiCamera()
led = LED(4)
text_button = Button(19)
object_button = Button(26)
location_buton = Button(6)
emergency_button = Button(13)

inst = ObjectDetect()
textInst = TextDetect()

def capture():
    
    led.on()
    camera.capture(imgpath)
    sleep(0.5)
    led.off()
    return imgpath


def obj_func():
    str1 = ("detecting please wait").encode()
    print(str1)
    ser.write(str1)
    objDetect = inst.localize_objects(capture())
    ser.write(objDetect.encode())
    print("The values are %s AND %s" % (objDetect, str2))

def text_func():
    str1 = ("reading please wait").encode()
    print(str1)
    ser.write(str1)
    str3 = textInst.text_within(capture())
    print("The values are %s AND %s" % (str3, str2))
    ser.write(str3.encode())
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

