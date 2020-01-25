import subprocess
import time
import serial

subprocess.Popen(['sudo','rfcomm','watch','hci0'])

print("doen")

time.sleep(3)
#ser = serial.Serial('/dev/rfcomm0')

