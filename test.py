from textToSpeech import my_speech
from gapi2 import output
from capture import capture
from faceDetect import face_main
from objectdetect import localize_objects

def read():
	my_speech("processing please wait")
	imgtxt = output()  # from gapi
	print(imgtxt)  # to test
	my_speech("the content is ")
	# make last part female voice
	my_speech(imgtxt) # from textTOSpeech
	

def objects():
	# should i use tensorflow for this ??????
	my_speech("detecting please wait")
	imgtxt = localize_objects("object.jpeg")  # from gapi
	print(imgtxt)  # to test
	my_speech("the content is ")
	# make last part female voice
	my_speech(imgtxt) # from textTOSpeech

def face():
# should i use tensorflow for this ??????
	my_speech("detecting please wait")
	faceData = face_main("faces.jpg","annote.jpg")
  # from gapi
	print(faceData)  # to test
	my_speech("the result is ")
	# make last part female voice
	my_speech(faceData) # from textTOSpeech



def control():
# paste all button conditions here
#needed to include ir remote also to the file
	pass

if __name__ =="__main__":
	objects()