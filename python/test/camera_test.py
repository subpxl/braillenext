import picamera
imgpath = "/home/pi/cashma/sample.jpg"
camera = picamera.PiCamera()
camera.rotation = 270
def capture():
    camera.start_preview()
    
    camera.capture(imgpath)
    print(imgpath)
    return imgpath


if __name__ == "__main__":
    capture()