
from textDetect import text_within
from faceDetect import loacalise_face
from objectdetect import ObjectDetect
from capture import capture
import serial
from gpiozero import Button
from signal import pause


#subprocess.Popen(['sudo','rfcomm','watch','hci0'])


ser = serial.Serial('/dev/rfcomm0')

face_button = Button(19)
text_button = Button(15)
object_button = Button(16)
location_buton = Button(17)
emergency_button = Button(18)

inst = ObjectDetect()

str1 = ("processing please wait").encode()
str2 = ("its completed").encode()

def face_func():

    # for testing
    print(str1)
    ser.write(str1)
    str3 = loacalise_face(capture()).encode()
    ser.write(str3)
    ser.write(str2)
    print("The values are %s AND %s" % (str3, str2))


def obj_func():
    print(str1)
    ser.write(str1)
    str3 = inst.localize_objects(capture()).encode()
    ser.write(str3)
    ser.write(str2)
    print("The values are %s AND %s" % (str3, str2))

def text_func():
    print(str1)
    ser.write(str1)
    str3 = text_within(capture()).encode()
    print("The values are %s AND %s" % (str3, str2))

    
    ser.write(str3)
    ser.write(str2)

def location_func():
    ser.write(("locationAsk").encode())


def emergency_func():
    ser.write(("emergencyAsk").encode())

# when the button is pressed
face_button.when_pressed = face_func
text_button.when_pressed = text_func
object_button.when_pressed = obj_func
location_buton.when_pressed = location_func
emergency_button.when_pressed = emergency_func

pause()


