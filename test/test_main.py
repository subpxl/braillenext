import textToSpeech
import unittest
import objectdetect
import faceDetect


Objimage = "images/testimages/truck.png"
Faceimage = "/home/pi/cashma/images/testimages/face.jpg"
FaceAnnotate = "/home/pi/cashma/images/testimages/annotate/annotate.jpg"
inst = objectdetect.ObjectDetect()
objres = inst.localize_objects(Objimage)

class test_cashma(unittest.TestCase):
  

        
    def test_speech(self):

        result = textToSpeech.mySpeechMale("Hiee")
        self.assertEqual(result,"Hiee")
    
    def test_object_detect(self):
        testString ="""number of object found is 2   they are 
Wheel (its accuracy is : 65.0 percent) and 
Tire (its accuracy is : 56.99999999999999 percent) and """
        self.assertMultiLineEqual(objres,testString)

    def test_face_detect(self):
        self.assertAlmostEqual(faceDetect.face_main(Faceimage,FaceAnnotate),"Found 1  faces")



if __name__ == '__main__':

    unittest.main()



