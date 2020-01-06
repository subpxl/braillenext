from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera = PiCamera()
button = Button(14)

filename ='sample.jpg'

def take_photo():
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture(filename)
    camera.stop_preview()

button.when_pressed = take_photo