from textToSpeech import mySpeechFemale,mySpeechMale
from gapi2 import output
from faceDetect import faceOutput
from objectdetect import localize_objects

def read():
	mySpeechMale("processing please wait")
	imgtxt = output()  # from gapi
	print(imgtxt)  # to test
	mySpeechMale("the content is ")
	# make last part female voice
	mySpeechFemale(imgtxt) # from textTOSpeech
	

def objects():
	# should i use tensorflow for this ??????
	mySpeechMale("detecting please wait")
	imgtxt = localize_objects("object.jpeg")  # from gapi
	print(imgtxt)  # to test
	mySpeechMale("the content is ")
	# make last part female voice
	mySpeechFemale(imgtxt) # from textTOSpeech

def face():
# should i use tensorflow for this ??????
	mySpeechMale("detecting please wait")
	faceData = faceOutput()
  # from gapi
	print(faceData)  # to test
	mySpeechMale("the result is ")
	# make last part female voice
	mySpeechFemale(faceData) # from textTOSpeech



def control():
# paste all button conditions here
#needed to include ir remote also to the file
	pass

if __name__ =="__main__":
	#face()
	read()