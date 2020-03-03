import unittest
from ..objectdetect import ObjectDetect, TextDetect
 

Objimage = "/home/pi/cashma/test/testimages/objects/truck.png"
Textimage = "/home/pi/cashma/test/testimages/text/sample.jpg"

inst = objectdetect.ObjectDetect()
objres = inst.localize_objects(Objimage)

textinst = TextDetect()
textTest = textinst.text_within(Textimage)

class test_cashma(unittest.TestCase):
  
    
    def test_object_detect(self):
        testString ="""number of object found is 2   they are 
Wheel (its accuracy is : 65.0 percent) and 
Tire (its accuracy is : 56.99999999999999 percent) and """
        self.assertMultiLineEqual(objres,testString)

#    def test_face_detect(self):
 #       self.assertAlmostEqual(faceDetect.face_main(Faceimage,FaceAnnotate),"Found 1  faces")

#    def test_text_detect(self):
 #       self.assertAlmostEqual()



if __name__ == '__main__':

    unittest.main()



