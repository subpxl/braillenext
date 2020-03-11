
import serial
import time
import os
import picamera
from time import sleep

#subprocess.Popen(['sudo','pkill','rfcomm'])
#subprocess.Popen(['sudo','rfcomm','watch','hci0'])



imgpath = "/home/pi/cashma/test/testimages/sample.jpg"
ser = serial.Serial('/dev/rfcomm0')


from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/keys/apikey.json"
import time


camera = picamera.PiCamera()

def capture():
    
    camera.capture(imgpath)
    print("i am called")
    return imgpath

image = capture()



class ObjectDetect():


    def localize_objects(self,path):
#        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        with open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)

        objects = client.object_localization(
        image=image).localized_object_annotations

        #   print('Number of objects found: {}'.format(len(objects)))

        print("class data called line 55")
    #    return 'Number of objects found: {}'.format(len(objects))
        if len(objects)>0:
            xx =""
            yy = "number of object found is {}   ".format(len(objects))
            zz = "they are "
            for object_ in objects:
                xx+= ('\n{} (its accuracy is : {} percent) and '.format(object_.name, (round(object_.score, 2)*100)))
            print("printing data : line 63")
            return yy+zz+xx

        else:
            return "no object found"


if __name__ == "__main__":

    inst = ObjectDetect()
    print("this is a test  for object")
    result= inst.localize_objects(image)
    print(result)
