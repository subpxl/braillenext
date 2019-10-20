from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/apikey.json"
import picamera
import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture










class ObjectDetect():

    def localize_objects(self,path):
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        with open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)

        objects = client.object_localization(
        image=image).localized_object_annotations

        #   print('Number of objects found: {}'.format(len(objects)))


    #    return 'Number of objects found: {}'.format(len(objects))
        if len(objects)>0:
            xx =""
            yy = "number of object found is {}   ".format(len(objects))
            zz = "they are "
            for object_ in objects:
                xx+= ('\n{} (its accuracy is : {} percent) and '.format(object_.name, (round(object_.score, 2)*100)))
            
            return yy+zz+xx

        else:
            return "no object found"
    def objectOutput(self):
        return localize_objects(object_file)



camera = picamera.PiCamera()


    i = 0
    while os.path.exists("image%s.jpg" % i):
        i += 1


    fh = open("sample%s.txt" % i, "w")
    camera.capture("sample%s.txt" % i)
    print(i)





app = App(title="Hello world")
welcome_message = Text(app, text="  CASHMA", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=readBook, text="READ")
app.display()