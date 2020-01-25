
import time
import serial
import subprocess

subprocess.Popen(['sudo','pkill','rfcomm'])

subprocess.Popen(['sudo','rfcomm','watch','hci0'])
time.sleep(5)
ser = serial.Serial('/dev/rfcomm0')

hh = ("""hi shubham panchal, 
this is frost""").encode()
ser.write(hh)
