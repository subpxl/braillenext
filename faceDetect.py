from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import os
from capture import captureFace
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/apikey.json"

face_filex = captureFace()


print(face_filex,type(face_filex))

#%%
def detect_face(face_file, max_results=100):
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)
    return client.face_detection(image=image, max_results=max_results).face_annotations
    
def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.

    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the
          faces have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    # Sepecify the font-family and the font-size
    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        # Place the confidence value/score of the detected faces above the
        # detection box in the output image
        draw.text(((face.bounding_poly.vertices)[0].x,
                   (face.bounding_poly.vertices)[0].y - 30),
                  str(format(face.detection_confidence, '.3f')) + '%',
                  fill='#FF0000')
    im.save(output_filename)

def  face_main(input_filename, output_filename, max_result=10):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_result)
  #      print('Found {} face{}'.format(
   #         len(faces), '' if len(faces) == 1 else 's'))

#        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)

        if len(faces) >0:
            return 'Found {}  faces'.format(len(faces))

        else:
            return " no face found"


def faceOutput():
    op =  face_main(face_filex,"annote.jpg")
    return op
    
if __name__ == "__main__":
    print(faceOutput())
