import picamera
import time

camera = picamera.PiCamera()

image = "images/image"+str(time.time())+".jpg"

def captureFace():
    camera.capture(image)
    return(image)

def captureDocs():
    camera.capture(image)
    return(image)



def captureObject():
    camera.capture(image)
    return(image)


print(captureDocs())