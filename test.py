from textToSpeech import my_speech
from gapi2 import output
from capture import



def read():
	my_speech("processing please wait")
	imgtxt = output()  # from gapi
	print(imgtxt)  # to test
	my_speech("the content is ")
	# make last part female voice
	my_speech(imgtxt) # from textTOSpeech

def objectDetect():
	# should i use tensorflow for this ??????
	my_speech("detecting please wait")
	imgtxt = output()  # from gapi
	print(imgtxt)  # to test
	my_speech("the content is ")
	# make last part female voice
	my_speech(imgtxt) # from textTOSpeech

def control():
# paste all button conditions here
#needed to include ir remote also to the file
if 

if __name__ =="__main__":
	control()