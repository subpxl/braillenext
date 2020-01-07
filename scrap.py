
from textDetect import text_within
from faceDetect import loacalise_face
from objectdetect import ObjectDetect
from capture import capture
import serial
from gpiozero import Button


ser = serial.Serial('/dev/rfcomm0')

face_button = Button(14)
text_button = Button(15)
object_button = Button(16)
location_buton = Button(17)
emergency_button = Button(18)



#print(text_within(capture()))
#print(loacalise_face(capture()))


inst = ObjectDetect()


def face_func():
    ser.write(loacalise_face(capture()).encode())

def obj_func():
    ser.write(inst.localize_objects(capture()).encode())

def text_func():
    ser.write(text_within(capture()).encode())

def location_func():
    ser.write(("locationAsk").encode())


def emergency_func():
    ser.write(("emergencyAsk").encode())

    
face_button.when_pressed = face_func
text_button.when_pressed = text_func
object_button.when_pressed = obj_func
location_buton.when_pressed = location_func
emergency_button.when_pressed = emergency_func



#inst = ObjectDetect()
#result= inst.localize_objects(capture())
#hh=result.encode()
#ser.write(hh)
#print(hh)