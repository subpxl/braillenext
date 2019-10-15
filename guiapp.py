from guizero import App, Text, TextBox, PushButton, Slider, Picture
from control import  read,face,objects
def readBook():
    read()
    #welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello world")

welcome_message = Text(app, text="  CASHMA", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=readBook, text="READ")



text_size = Slider(app, command=change_text_size, start=10, end=80)
#my_cat = Picture(app, image="cat.gif")

app.display()