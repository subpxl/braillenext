import picamera
from time import sleep
from gpiozero import Button
import serial
from textDetect import text_within
from faceDetect import loacalise_face
from objectdetect import ObjectDetect
from capture import capture
#ser = serial.Serial('/dev/rfcomm0')

camera = picamera.PiCamera()
imgpath = "/home/pi/cashma/images/testimages/sample.jpg"

def capture():
    i = 0
    i =i+1
    camera.capture(imgpath)

#camera = PiCamera()

face_button = Button(14)
text_button = Button(15)
object_button = Button(16)
location_buton = Button(17)
emergency_button = Button(18)


text_path = '/home/pi/cashma/images/testimages/text/text.jpg'
face_path= '/home/pi/cashma/images/testimages/face/face.jpg'
object_path = '/home/pi/cashma/images/testimages/objects/truck.png'


def take_photo():
    #camera.start_preview(alpha=190)
    sleep(1)
    camera.capture(imgpath)
    camera.stop_preview()

#button.when_pressed = take_photo

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

#aa = loacalise_face(face_path)
##aa = read_text(text_path)
#inst = ObjectDetect()
#result= inst.localize_objects(object_path)

#take_photo()
if __name__ == "__main__":
  print(capture())
