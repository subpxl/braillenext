#! /usr/bin/python
#subprocess.Popen(['sudo','rfcomm','watch','hci0'])
#subprocess.Popen(['sudo','hciconfig','hci0','piscan'])

import serial
import time
ser = serial.Serial('/dev/rfcomm0')

hhh=("#emergencyAsk").encode()

ll =("#locationAsk").encode()
# vars = hhh ,ll
ser.write(("offcourse I love you").encode())
time.sleep(2)

ser.write(ll)
time.sleep(5)
ser.write(hhh)

print("done")

