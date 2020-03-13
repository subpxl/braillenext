
from objectdetect import ObjectDetect, TextDetect
import serial
from gpiozero import Button, LED
from signal import pause
import subprocess
import time
import os
import picamera
from time import sleep

#subprocess.Popen(['sudo','pkill','rfcomm'])
#subprocess.Popen(['sudo','rfcomm','watch','hci0'])



imgpath = "/home/pi/cashma/test/testimages/sample.jpg"
ser = serial.Serial('/dev/rfcomm0')
welcome = (" the machine is connected").encode()

print(welcome)
ser.write(welcome)


led = LED(17)
camera = picamera.PiCamera()
text_button = Button(19)
object_button = Button(26)
location_buton = Button(6)
emergency_button = Button(13)


def lightOn():
    led.on()
    print("on")
    sleep(2)

def lightOff():
    
    led.off()
    print("off")



lightOn()
lightOff()



inst = ObjectDetect()
textInst = TextDetect()

def capture():
    camera.start_preview()
    lightOn()
    camera.capture(imgpath)
    lightOff()
    return imgpath




def obj_func():
    str1 = ("detecting object please wait").encode()
    print(str1)
    ser.write(str1)
 #   led.on()
    objDetect = inst.localize_objects(capture())
  #  led.off()
    ser.write(objDetect.encode())
    print("The values are %s " % (objDetect))

def text_func():
    str1 = ("reading text please wait").encode()
    str2 = ("the content is ").encode()
    print(str1)
    ser.write(str1)
   # led.on()
    str3 = textInst.text_within(capture())
    #led.off()
    print("The values are %s AND %s" % (str3, str2))
    ser.write(str2)
    time.sleep(1)
    ser.write(str3.encode())
    

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

