import picamera
import time

camera = picamera.PiCamera()

face = "images/face/face"+str(time.time())+".jpg"

docs = "images/text/docs"+str(time.time())+".jpg"

objs = "images/object/obj"+str(time.time())+".jpg"

def captureFace():
    camera.capture(face)
    return(face)

def captureDocs():
    camera.capture(docs)
    return(docs)


def captureObject():
    camera.capture(objs)
    return(objs)
