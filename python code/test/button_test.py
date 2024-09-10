from gpiozero import Button

#26 19 13 6 5
button1 = Button(19)    #working
button4 = Button(13)   #working
button3 = Button(6) #working
button2 = Button(26) #working




while True:
    if button2.is_pressed:
        print("Button2 is pressed")
    
    if button1.is_pressed:
        print("Button1 is pressed")
    
    if button4.is_pressed:
        print("Button4 is pressed")
    
    if button3.is_pressed:
        print("Button3 is pressed")
 
    
    else:
        print("Button is not pressed")


