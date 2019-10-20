import picamera
import time

camera = picamera.PiCamera()

i = 0
while os.path.exists("image%s.jpg" % i):
    i += 1


fh = open("sample%s.txt" % i, "w")
camera.capture("sample%s.txt" % i)
print(i)


