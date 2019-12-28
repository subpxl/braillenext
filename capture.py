import picamera
import time
import os

camera = picamera.PiCamera()
imgpath = "/home/pi/cashma/images/testimages/sample.jpg"

def capture():
    i = 0
    try:
        i =i+1
        camera.capture(imgpath)
        return imgpath
    
    except:
       return("some issue")

    finally:
        pass


  #  while os.path.exists("/home/pi/cashma/images/testimages/sample%s.jpg" % i):
   #     i += 1
    #    imaged = "/home/pi/cashma/images/testimages/sample{}.jpg".format(i)
     #   print(imaged)
      #  camera.capture(imaged)
       # camera.close()
        #print(i)



if __name__ == "__main__":
  print(capture())
