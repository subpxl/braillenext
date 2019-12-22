import textToSpeech
import unittest
import objectdetect



image = "images/testimages/truck.png"
inst = objectdetect.ObjectDetect()
objres = inst.localize_objects(image)

class test_cashma(unittest.TestCase):
  

        
    def test_speech(self):

        result = textToSpeech.mySpeechMale("Hiee")
        self.assertEqual(result,"Hiee")
    
    def test_object_detect(self):
        self.assertIsNot(objres,None)




if __name__ == '__main__':

    unittest.main()



