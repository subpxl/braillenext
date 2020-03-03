from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/keys/apikey.json"
import time

image = '/home/pi/cashma/images/testimages/objects/truck.png'

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


class TextDetect(object):


    def text_within(self, path): 
        text=""
        x1 =50
        y1 = 0
        x2 = 8331
        y2 = 4000
        client = vision.ImageAnnotatorClient()
        with io.open(path, 'rb') as image_file2:
            content = image_file2.read()

        content_image = types.Image(content=content)
        response = client.document_text_detection(image=content_image)
        document = response.full_text_annotation

        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            min_x=min(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                            max_x=max(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                            min_y=min(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                            max_y=max(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                            if(min_x >= x1 and max_x <= x2 and min_y >= y1 and max_y <= y2):
                                text+=symbol.text
                                if(symbol.property.detected_break.type==1 or 
                                symbol.property.detected_break.type==3):
                                    text+=' '
                                if(symbol.property.detected_break.type==2):
                                    text+='\t'
                                if(symbol.property.detected_break.type==5):
                                    text+='\n'
        return text


if __name__ == "__main__":

    inst = ObjectDetect()
    result= inst.localize_objects(image)
    print(result)

