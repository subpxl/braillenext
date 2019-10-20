import picamera
import time
import os
camera = picamera.PiCamera()

i = 0
while os.path.exists("/home/pi/cashma/images/image%s.jpg" % i):
    i += 1


    fh = open("sample%s.txt" % i, "w")
    camera.capture("sample%s.jpg" % i)
    print(i)


