
import serial
from gpiozero import Button
from signal import pause
import subprocess
import time
import os
from main import location_func , emergency_func

try:
    location_func()
    emergency_func()
except :
    print("failed")
finally:
    print("test done")