from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/apikey.json"

<<<<<<< HEAD
=======




>>>>>>> night 10 august
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

    
    for object_ in objects:
        #xx = ('\n{} (confidence: {})'.format(object_.name, object_.score))
        xx = ((object_.name, object_.score))
    
    return xx
#    objList = [[object_.name, object_.score] for object_ in objects]
 #   return objList

