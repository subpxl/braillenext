from gpiozero import LED
from time import sleep
from signal import pause
led = LED(17)

while True:
    led.on()
    print("on")
    sleep(1)
    led.off()
    print("off")
    sleep(1)



    