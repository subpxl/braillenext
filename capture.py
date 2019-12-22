import picamera
import time
import os
camera = picamera.PiCamera()



print(os.getcwd())
#camera.capture("images/sample.jpg" )
i = 0

while os.path.exists("sample%s.jpg" % i):
    i += 1
    imaged = "sample{}.jpg".format(i)
    camera.capture(imaged)
    print(i)



