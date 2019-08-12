from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
from capture import captureObject
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/apikey.json"

object_file = captureObject()
def localize_objects(path):
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
def objectOutput():
    return localize_objects(object_file)

