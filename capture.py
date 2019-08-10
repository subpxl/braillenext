import picamera
import time
camera = picamera.PiCamera()

def capture():
    camera.capture('example.jpg')


if __name__ == "__main__":
    capture()