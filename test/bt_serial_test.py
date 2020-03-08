#! /usr/bin/python
#subprocess.Popen(['sudo','rfcomm','watch','hci0'])
#subprocess.Popen(['sudo','hciconfig','hci0','piscan'])

import serial

ser = serial.Serial('/dev/rfcomm0')

hhh="bluetooth serial test success"

hh=hhh.encode()
ser.write(hh)


