from picamera import PiCamera
from time import sleep
from gpiozero import Button
import serial
from textDetect import text_within
from faceDetect import loacalise_face
from objectdetect import ObjectDetect

ser = serial.Serial('/dev/rfcomm0')


#camera = PiCamera()
button = Button(14)

text_path = '/home/pi/cashma/images/testimages/text/text.jpg'
face_path= '/home/pi/cashma/images/testimages/face/face.jpg'
object_path = '/home/pi/cashma/images/testimages/objects/truck.png'

def take_photo():
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture(filename)
    camera.stop_preview()

button.when_pressed = take_photo

def read_text(document):
    textlen =text_within(document) 
    print(textlen)
    if len(textlen)>=1:
        pass
    else:
        print( "no text found")

def read_object(image):
    obj = ObjectDetect()
    result = obj.localize_objects(image)
    return result

def read_face(image):
    result = loacalise_face(image)
    return result


def send_data(hhh):
    hh=hhh.encode()
    ser.write(hh)
    return None


#subprocess.Popen(['sudo','rfcomm','watch','hci0'])


send_data("goo")
aa = loacalise_face(face_path)
print(aa)
send_data(aa)
send_data("DONE")



send_data("goo")
aa = read_text(text_path)
print(aa)
send_data(aa)
send_data("DONE")



send_data("goo")
inst = ObjectDetect()
result= inst.localize_objects(object_path)
print(result)
send_data(result)
send_data("DONE")
