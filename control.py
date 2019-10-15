from textToSpeech import mySpeechMale
from gapi2 import output
from faceDetect import faceOutput
from objectdetect import objectOutput
from guizero import App, Text, TextBox, PushButton, Slider, Picture




def read():
	mySpeechMale("processing please wait")
	imgtxt = output()  # from gapi
	print(imgtxt)  # to test
	mySpeechMale("the content is ")
	# make last part female voice
	mySpeechMale(imgtxt) # from textTOSpeech
	

def objects():
	# should i use tensorflow for this ??????
	mySpeechMale("detecting please wait")
	objtxt = objectOutput()  # from gapi
	print(objtxt)  # to test
	mySpeechMale("the content is ")
	# make last part female voice
	mySpeechMale(objtxt) # from textTOSpeech

def face():
# should i use tensorflow for this ??????
	mySpeechMale("detecting please wait")
	faceData = faceOutput()
  # from gapi
	print(faceData)  # to test
	mySpeechMale("the result is ")
	# make last part female voice
	mySpeechMale(faceData) # from textTOSpeech

app = App(title="Hello world")
welcome_message = Text(app, text="  CASHMA", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=read, text="READ")


app.display()
