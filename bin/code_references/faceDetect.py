from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/keys/apikey.json"
image = '/home/pi/cashma/images/testimages/face/face.jpg'
annotate_path = "/home/pi/cashma/images/testimages/annotate/annotate.jpg"

    

def detect_face(face_file, max_results=100):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)
    countNo= client.face_detection(image=image, max_results=max_results).face_annotations
    return countNo

def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    for face in faces:
        box = [(vertex.x, vertex.y)
            for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        draw.text(((face.bounding_poly.vertices)[0].x,
                (face.bounding_poly.vertices)[0].y - 30),
                str(format(face.detection_confidence, '.3f')) + '%',
                fill='#FF0000')
    im.save(output_filename)


# this is for face image annotation
def  face_main(input_filename, output_filename, max_results=10):
    
    with open( input_filename, 'rb') as image:
        
        faces = detect_face(image, max_results)
        image.seek(0)
        highlight_faces(image, faces, output_filename)

        if len(faces) >0:
            return 'Found {}  faces'.format(len(faces))

        else:
            return " no face found"

# this is for no data saving
def  loacalise_face(input_filename, max_results=10):
    
    with open( input_filename, 'rb') as image:
        
        faces = detect_face(image, max_results)
        image.seek(0)

        if len(faces) >0:
            return 'Found {}  faces'.format(len(faces))

        else:
            return " no face found"



"""def faceOutput():
    op =  face_main(image,annotate_path)
    return op"""



if __name__ == "__main__":

    print(loacalise_face(image))