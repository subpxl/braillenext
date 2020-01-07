import picamera
import time
import os

camera = picamera.PiCamera()
imgpath = "/home/pi/cashma/images/testimages/sample.jpg"

def capture():
    i = 0
    i =i+1
    camera.capture(imgpath)
   # camera.close()


    return imgpath
 
  #  while os.path.exists("/home/pi/cashma/images/testimages/sample%s.jpg" % i):
   #     i += 1
    #    imaged = "/home/pi/cashma/images/testimages/sample{}.jpg".format(i)
     #   print(imaged)
      #  camera.capture(imaged)
       # camera.close()
        #print(i)



if __name__ == "__main__":
  print(capture())
